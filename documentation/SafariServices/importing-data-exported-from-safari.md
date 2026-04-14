# Importing data exported from Safari

**Framework**: Safari Services

Transfer bookmarks, saved passwords, and other information between browsers.

#### Overview

In iOS, iPadOS, and visionOS, people can export their browser data to a file from Safari’s settings in Settings. In macOS, the person exports Safari’s browser data by choosing File > Export from Safari. In either case, the system presents the Export Browsing Data sheet, which walks the person through the export process. Alternatively, you can present the export sheet from a browser app that you develop by calling the [`SFSafariSettings`](sfsafarisettings.md) class’s [`openExportBrowsingDataSettings(completionHandler:)`](sfsafarisettings/openexportbrowsingdatasettings(completionhandler:).md) method.

Safari exports the data in a ZIP archive that contains a bookmarks file, a passwords file, and a payment cards file. For each Safari profile, the ZIP archive also includes a browser history file and a Safari extensions file. The files have localized file names; in the `en_US` locale, their names are:

- **Bookmark data**: `Bookmarks.html`
- **Passwords**: `Passwords.csv`
- **Browser history**: `History.json`
- **Payment cards**: `PaymentCards.json`
- **Safari extensions**: `Extensions.json`

When someone creates multiple profiles, Safari exports the browser history and extension information for each profile into a separate file with the profile name as a filename suffix.

To import this data, create UI in your browser that someone uses to share the ZIP archive they export from Safari. Unzip the file, and use the information in the sections below to interpret the contents that you load into your browser’s data model.

Your browser can also export its data in the same format for someone to import into Safari.

##### Import Bookmarks and Reading List

Safari exports bookmarks in an HTML file using the [`Netscape Bookmarks file format`](https://developer.apple.comhttps://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753582(v=vs.85)). The Reading List is a sub-folder with the identifier `com.apple.ReadingList`.

##### Import Safari Passwords

Safari exports passwords in a comma-separated values (CSV) file that includes a titles row and contains the following columns:

- **`Title`**: A name for the saved password.
- **`URL`**: A URL for the website that someone saved the password for.
- **`Username`**: The username associated with the password.
- **`Password`**: The saved password.
- **`Notes`**: Free-form notes that the person associated with the password.
- **`OTPAuth`**: A URL that uses the otpauth scheme and identifies the one-time passcode (OTP) generator that the website uses as a second factor with the password, for example, `otpauth://totp?secret=ASDFA&algorithm=SHA1&digits=6&period=30`.

##### Understand Json Metadata

Safari exports browser history, extensions, and payment cards as JSON files. The top-level object in each file contains a `metadata` key, whose value is a JSON object containing these keys:

- **`browser_name`**: A string that’s web browser name, which is `Safari` if someone exported the data from Safari on iOS, iPadOS, macOS, or visionOS; or `Safari Technology Preview` if someone exported the data from Safari Technology Preview on macOS.
- **`browser_version`**: A string that’s the version of Safari that exported the data, for example `18.2`.
- **`data_type`**: A string that describes the data in the file; one of `history`, `extensions`, or `payment_cards`.
- **`export_time_usec`**: An integer that’s the UNIX timestamp (the number of microseconds since midnight in the UTC time zone on January 1, 1970) at which Safari exported the file.
- **`schema_version`**: An integer that’s the version of the export schema.

##### Import Browser History

The top-level object in the history JSON file contains a `history` key, which has a value that is an array of objects representing websites that Safari visited. Each object in the array contains these keys:

- **`url`**: A string that’s the URL of the history item.
- **`title`**: An optional string that, if present, is the title of the history item.
- **`time_usec`**: An integer that’s the UNIX timestamp in microseconds of the latest visit to the item.
- **`destination_url`**: An optional string that, if present, is the URL of the next item in the redirect chain.
- **`destination_time_usec`**: An optional integer that’s present if `destination_url` is also present and is the UNIX timestamp (the number of microseconds since midnight UTC, January 1, 1970) of the next navigation in the redirect chain.
- **`source_url`**: An optional string that, if present, is the URL of the previous item in the redirect chain.
- **`source_time_usec`**: An optional integer that’s present if `source_url` is also present and is the UNIX timestamp in microseconds of the previous navigation in the redirect chain.
- **`visits_count`**: An integer that’s the number of visits the browser made to this item, and is always greater than or equal to `1`.
- **`latest_visit_was_load_failure`**: An optional Boolean that’s `true` if Safari failed to load the site when someone most recently tried to access it; otherwise, it’s `false`.
- **`latest_visit_was_http_get`**: An optional Boolean that’s `true` if the last visit to this item used the HTTP `GET` method; otherwise, it’s `false`.

When the web server redirects Safari to a different URL, the history list contains all of the URLs in the chain of redirections. Link items in the redirection chain by comparing the `url` and `time_usec` fields in one history item with the `destination_url` and `destination_time_usec` of the item that redirected Safari to it, and the `source_url` and `source_time_usec` of the item that it redirected Safari to, for example:

```javascript
...
{
   "url" : "https://maps.apple.com/",
   "time_usec" : 1722367302951213,
   "destination_url" : "https://www.apple.com/maps/",
   "destination_time_usec" : 1722367302951310
},
{
   "url" : "https://www.apple.com/maps/",
   "time_usec" : 1722367302951310,
   "title" : "Maps - Apple",
   "source_url" : "https://maps.apple.com/",
   "source_time_usec" : 1722367302951213
},
...
```

##### Import Payment Cards

The top-level object in the payment cards JSON file contains a `payment_cards` key, which has a value that is an array of objects representing the payment cards the person stored in Safari. Each object in the array contains these keys:

- **`card_number`**: A string that is the payment card number.
- **`card_name`**: An optional string that, if present, is the name the person gave to the payment card.
- **`cardholder_name`**: An optional string that, if present, is the name of the cardholder.
- **`card_expiration_month`**: An optional integer that, if present, is the month of the card’s expiration date.
- **`card_expiration_year`**: An optional integer that, if present, is the year of the card’s expiration date.
- **`card_last_used_time_usec`**: An optional integer that, if present, is the UNIX timestamp of the most recent occasion the person used the payment card.

The object looks like this example:

```javascript
{
  "card_number" : "0000000000000000",
  "card_name" : "My Bank Card",
  "cardholder_name" : "Mei Chen",
  "card_expiration_month" : 11,
  "card_expiration_year" : 2027,
  "card_last_used_time_usec" : 1722730594744987
}
```

##### Import Extension Information

The top-level object in the extensions JSON file contains an `extensions` key, which has a value that is an array of objects representing the Safari App Extensions, Safari Web Extensions, and Safari Content Blockers that the person installed and enabled in their Safari profile. Each object in the array contains these keys:

- **`composed_identifier`**: A string that’s the bundle identifier of the extension followed by the Developer Team ID, for example `com.example.great-app.browser-extension (AB67HSA2XZ)`.
- **`developer_name`**: A string that’s the name of the extension’s developer.
- **`display_name`**: A string that’s the display name of the extension.
- **`marketplace_lookup`**: A JSON object that contains information you use to discover the extension’s containing app in its marketplace, which for Safari extensions is the App Store or Mac App Store.

The `marketplace_lookup` object contains these keys:

- **`store_identifier`**: A string that’s the identifier in the marketplace for the app that contains the Safari extension.
- **`ios_extension_bundle_identifier`**: A string that, if present, is the bundle identifier of the Safari extension on iOS corresponding with this Safari extension on macOS.
- **`ios_app_bundle_identifier`**: A string that, if present, is the bundle identifier of the iOS app corresponding with the macOS app that hosts this Safari extension.
- **`macos_extension_bundle_identifier`**: A string that, if present, is the bundle identifier of the Safari extension on macOS corresponding with this Safari extension on iOS.
- **`macos_app_bundle_identifier`**: A string that, if present, is the bundle identifier of the macOS app corresponding with the iOS app that hosts this Safari extension.

For more information on bundle identifiers, see [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier).

## See Also

- [class SFSafariViewController](sfsafariviewcontroller.md)
  An object that provides a visible standard interface for browsing the web.
- [SFAuthenticationSession.CompletionHandler](sfauthenticationsession/completionhandler.md)
  The completion handler for an authentication session when the user cancels or finishes the login.
- [class SFSafariSettings](sfsafarisettings.md)
  A class that provides your app access to several of Safari’s settings options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/importing-data-exported-from-safari)*