# Importing data exported from Safari

**Framework**: Safari Services

Transfer bookmarks, saved passwords, and other information between browsers.

#### Overview

Starting in iOS 18.2, iPadOS 18.2, and visionOS 2.2, someone can export their browser data from Safari Settings in the Settings app. In macOS 15.2 and newer, they export their browser data by choosing File > Export in Safari.

On all platforms, Safari exports the data in a ZIP archive that contains a bookmarks file, a passwords file, a payment cards file, and for each profile the person creates in Safari one browser history file and one Safari extensions file. The files have localized file names, in the `en_US` locale their names are:

When someone creates multiple profiles, Safari exports the browser history and extension information for each profile into a separate file with the profile name as a filename suffix.

To import this data, create UI in your browser that someone uses to share the ZIP archive they export from Safari. Unzip the file, and use the information in the sections below to interpret the contents that you load into your browser’s data model.

Your browser can also export its data in the same format for someone to import into Safari.

##### Import Bookmarks and Reading List

Safari exports bookmarks in an HTML file using the [`Netscape Bookmarks file format`](https://developer.apple.comhttps://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753582(v=vs.85)). The Reading List is a sub-folder with the identifier `com.apple.ReadingList`.

##### Import Safari Passwords

Safari exports passwords in a comma-separated values (CSV) file that includes a titles row and contains the following columns:

##### Understand Json Metadata

Safari exports browser history, extensions, and payment cards as JSON files. The top-level object in each file contains a `metadata` key, whose value is a JSON object containing these keys:

##### Import Browser History

The top-level object in the history JSON file contains a `history` key, which has a value that is an array of objects representing websites that Safari visited. Each object in the array contains these keys:

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

The `marketplace_lookup` object contains these keys:

For more information on bundle identifiers, see [`CFBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIdentifier).

## See Also

- [class SFSafariViewController](sfsafariviewcontroller.md)
  An object that provides a visible standard interface for browsing the web.
- [SFAuthenticationSession.CompletionHandler](sfauthenticationsession/completionhandler.md)
  The completion handler for an authentication session when the user cancels or finishes the login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/importing-data-exported-from-safari)*