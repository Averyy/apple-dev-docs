# TN3147: Migrating to the latest notarization tool

**Framework**: Technotes

Migrate your notarization workflows to `notarytool` from the deprecated `altool`.

#### Overview

At [`WWDC 2021`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10261/) Apple introduced `notarytool`, a new tool for interacting with the Apple notary service.  When it comes to notarization, this tool is faster and more reliable than the previous `altool`.  If you’re still notarizing with `altool`, it’s time to switch to `notarytool`.

> ❗ **Important**: Apple has deprecated `altool` for the purposes of notarization and [`announced that it will stop working for notarization on 2023-11-01`](https://developer.apple.comhttps://developer.apple.com/news/?id=y5mjxqmn).  However, `altool` is still a good way to perform other tasks, like submitting an app to the App Store.

To migrate your workflows to `notarytool`:

1. Get the new tool.
2. Migrate the credentials you use to authenticate with the notary service.
3. Test your new credentials.
4. Adopt `notarytool` for each notarization operation you use.

You can use `altool` and `notarytool` in parallel.  Feel free to leave your current notarization workflow in place while you experiment with `notarytool`.  Then, when you’re happy with the new workflow, cut over to `notarytool`.  Just make sure you do this before the above-mentioned deadline.

If you’re not migrating from `altool`—that is, you’re setting up notarization for the first time—ignore this technote and instead start with [`Notarizing macOS software before distribution`](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution) and then move on to [`Customizing the notarization workflow`](https://developer.apple.com/documentation/Security/customizing-the-notarization-workflow).  Or, if you want to notarize from a non-Apple platform, see [`Notary API`](https://developer.apple.comhttps://developer.apple.com/documentation/notaryapi).

#### Get the New Tool

If you have Xcode 13 or later then you already have `notarytool`.  Just run it with `xcrun`:

```shell
% xcrun notarytool
OVERVIEW: Manage submissions to the Apple notary service
…
```

If `xcrun` can’t find the tool, make sure you have Xcode 13 or later selected:

```shell
% xcode-select --print-path
/Applications/Xcode.app/Contents/Developer
```

If not, select it using the `--switch` command:

```shell
% sudo xcode-select --switch ~/MyXcodeInstalls/Xcode13.app
```

If you want to keep an older version of Xcode selected but use `notarytool` from the newer one, set the `DEVELOPER_DIR` environment variable when you invoke `xcrun`:

```shell
% DEVELOPER_DIR=~/MyXcodeInstalls/Xcode13.app/Contents/Developer xcrun notarytool
OVERVIEW: Manage submissions to the Apple notary service
…
```

If your version of macOS does not support Xcode 13, see [`Enable notarization on an older version of macOS`](tn3147-migrating-to-the-latest-notarization-tool#Enable-notarization-on-an-older-version-of-macOS.md).

#### Migrate Your Credentials

`notarytool` supports the same credentials as `altool`: an app-specific password or an App Store Connect API key.

##### App Specific Password

If you’re currently authenticating with an app-specific password, your `altool` commands might start like this:

```shell
% xcrun altool --username APPLE_ID --team-id TEAM_ID --password PASSWORD …
```

> **Note**: All the examples here use long-format options, so `--username` rather than `-u`.  If you’re currently using short-format options, run `altool` with the `--help` option to see the mapping.

In this command:

- `APPLE_ID` is your Apple ID.
- `TEAM_ID` is your Team ID.  You might be using the older `--asc-provider` or `--asc-public-id` options for this.
- `PASSWORD` is your app-specific password.

The equivalent for `notarytool` is:

```shell
% xcrun notarytool … --apple-id APPLE_ID --team-id TEAM_ID --password PASSWORD …
```

Here `APPLE_ID`, `TEAM_ID`, and `PASSWORD` are as above.

If your Apple ID only belongs to one team then you don’t need to supply a Team ID.  However, it’s best practice to include it regardless.  That way, joining another team at some point in the future won’t break your notarization workflow.  To find your Team ID, go to the [`Account page`](https://developer.apple.comhttps://developer.apple.com/account) on the Apple Developer website.

You can use the same app-specific password for both `altool` and `notarytool`.  You might also choose to create a new app-specific password for `notarytool`.  To do that, follow the steps in [`Using app-specific passwords`](https://developer.apple.comhttps://support.apple.com/en-us/HT204397).

> **Note**: If you use the `@keychain` prefix to tell `altool` to get the password from a keychain item, see [`Save credentials in the keychain`](tn3147-migrating-to-the-latest-notarization-tool#Save-credentials-in-the-keychain.md).

##### App Store Connect Api Key

If you’re currently authenticating with an App Store Connect API key, your `altool` commands might start like this:

```shell
% xcrun altool --username APPLE_ID --apiIssuer ISSUER_UUID --apiKey API_KEY …
```

In this command:

- `APPLE_ID` is your Apple ID.
- `ISSUER_UUID` is your App Store Connect API key issuer, for example, `c055ca8c-e5a8-4836-b61d-aa5794eeb3f4`.
- `API_KEY` is your App Store Connect API key ID, for example, T9GPZ92M7K.

`altool` uses the key ID to search for the key’s `.p8` file.  For example, it might find a key file at `~/.appstoreconnect/private_keys/AuthKey_T9GPZ92M7K.p8`.

> **Note**: For details on the search path used by `altool`, see its man page.  If you’re unfamiliar with man pages, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

The equivalent for `notarytool` is:

```shell
% xcrun notarytool … --issuer ISSUER_UUID --key-id API_KEY --key PATH_TO_KEY …
```

Here `ISSUER_UUID` and `API_KEY` are as above, and `PATH_TO_KEY` is the path to the key’s `.p8` file.  There’s no need to supply your Apple ID because `notarytool` works that out based on the issuer.

It’s fine to use the same App Store Connect API key `.p8` file for both `altool` and `notarytool`.  If you previously stored your key in `~/.appstoreconnect/private_keys/AuthKey_API_KEY.p8`, just pass that path to the `--key` option.

#### Test Your Credentials

The best way to test your credentials is to get a history of recent activity.  In `altool` you might use a command like this:

```shell
% xcrun altool OLD_CREDENTIALS --notarization-history 0
```

In this command, `OLD_CREDENTIALS` is your existing `altool` credentials.

To test out your `notarytool` credentials, pass them to the `history` subcommand:

```shell
% xcrun notarytool history NEW_CREDENTIALS
```

Replace `NEW_CREDENTIALS` with the new credentials you worked out in the previous section.

> **Note**: Each tool maintains its own separate history.  If this is the first time you’ve used `notarytool`, your history will be empty.

#### Convert Your Notarization Operations

Once you have your credentials sorted out, it’s time to replace each invocation of `altool` with the equivalent one for `notarytool`.  The common notarization operations are:

- Submit a file to the notary service
- Check on the status of a previous submission
- Fetch the notary log
- Get a history of recent activity

Remember that `notarytool` only replaces the notarization aspects of `altool`.  If you use `altool` for other tasks, like submitting an app to the App Store, continue to use it for that.

##### Submit a File

When using `altool`, your command to submit a file to the notary service might look like this:

```shell
% xcrun altool OLD_CREDENTIALS --notarize-app --file PATH_TO_FILE --primary-bundle-id BUNDLE_ID
```

In this example, `OLD_CREDENTIALS` is your existing `altool` credentials, `PATH_TO_FILE` is the path of the file you want to notarize, and `BUNDLE_ID` is the bundle ID of the main product in this file.

To do the same with `notarytool`, use the `submit` subcommand:

```shell
% xcrun notarytool submit NEW_CREDENTIALS PATH_TO_FILE
```

Here `PATH_TO_FILE` is as above.  Replace `NEW_CREDENTIALS` with the credentials from earlier.

> **Note**: There’s no replacement for the `--primary-bundle-id` option.  The notary service never interpreted that value; it was effectively a comment.

For a nice bonus, consider adding the `--wait` option.  With that, `notarytool` won’t return until the notarization is complete and, when it does return, it will output the submission’s status.  If you were previously polling the status to check for completion, add the `--wait` option and remove that logic.

##### Check Status

When using `altool`, your command to check the status of a submission might look like this:

```shell
% xcrun altool OLD_CREDENTIALS --notarization-info SUBMISSION_ID
```

In this example, `OLD_CREDENTIALS` is your existing `altool` credentials and `SUBMISSION_ID` is the submission ID you got when you submitted the file.

To do the same with `notarytool`, use the `info` subcommand:

```shell
% xcrun notarytool info NEW_CREDENTIALS SUBMISSION_ID
```

Here `SUBMISSION_ID` is as above.  Replace `NEW_CREDENTIALS` with the credentials from earlier.

> ❗ **Important**: If you currently poll the status to check whether a submission is complete, adopt the `--wait` option, as discussed in the previous section.  Once you do that, you may not need to use the `info` command at all.

The submissions IDs returned by `notarytool` live in a different namespace than those returned by `altool`.  You can’t check on the status of an `altool` submission with `notarytool`, or vice versa.

##### Fetch the Notary Log

After processing your submission the notary service generates a log.  This JSON file holds information about your submission, including errors and warnings.

> ❗ **Important**: Always check the notary log, even if notarization succeeds, because it might contain warnings that you can fix prior to your next submission.

Fetching the notary log with `altool` is a little convoluted.  You first get the status of the request.  If the request is finished, that status includes a `LogFileURL` property.  To get the log, fetch that URL with your preferred HTTP tool, for example, Safari or `curl`.

Things are much easier with `notarytool`.  To fetch the notary log, use the `log` subcommand:

```shell
% xcrun notarytool log NEW_CREDENTIALS SUBMISSION_ID
```

Replace `SUBMISSION_ID` with the submission ID you got when you submitted the file and `NEW_CREDENTIALS` with the credentials from earlier.

##### Get History

When using `altool`, your command to view a list of recent notarization requests might look like this:

```shell
% xcrun altool OLD_CREDENTIALS --notarization-history 0
```

To do the same with `notarytool`, use the `history` subcommand:

```shell
% xcrun notarytool history NEW_CREDENTIALS
```

Replace `NEW_CREDENTIALS` with the credentials from earlier.

#### Going Further

The new tool has a number of other features to make your life easier.

##### Getting Help

To get a list of commands, run `notarytool` with no arguments:

```shell
% xcrun notarytool
OVERVIEW: Manage submissions to the Apple notary service

SUBCOMMANDS:
…
  submit                  Submit an archive to the Notary service
…
```

To get help on a specific command, run that command with the `--help` option:

```shell
% xcrun notarytool submit --help
OVERVIEW: Submit an archive to the Notary service

USAGE: notarytool submit [<options>] <file-path>

ARGUMENTS:
  <file-path>             Path to the archive

OPTIONS:
…
```

For comprehensive help, see the `notarytool` man page.  If you’re unfamiliar with man pages, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

##### Save Credentials in the Keychain

With `altool`, you might have used the `--store-password-in-keychain-item` command to save an app-specific password in the keychain and then referenced it using the `@keychain` prefix.   `notarytool` supports the same workflow, with a slightly different syntax.

To start, use the `store-credentials` subcommand to save your app-specific password to the keychain:

```shell
% xcrun notarytool store-credentials PROFILE --apple-id APPLE_ID --team-id TEAM_ID
…
App-specific password for APPLE_ID: 
…
Credentials saved to Keychain.
To use them, specify `--keychain-profile "PROFILE"`
```

In this command:

- `PROFILE` is a name that you assign to these credentials.  You might use a value like `MyNotarizationPassword`.
- `APPLE_ID` is your Apple ID.
- `TEAM_ID` is your Team ID.

The command prompts you to enter your app-specific password.  Once you do that, it checks that the password is valid and, if so, stores the credentials in your keychain with the specified profile.

To use these credentials in subsequent commands, supply the profile name using the `--keychain-profile` option.  For example, to get a notarization history:

```shell
% xcrun notarytool history --keychain-profile PROFILE
```

> **Note**: Unless you specify a file-based keychain with the `--keychain` option, `notarytool` uses the data protection keychain.  To see stored credentials in that case, run Keychain Access, select iCloud Keychain on the left—or Local Items, if iCloud Keychain is not enabled—and look for items named `com.apple.gke.notary.tool`.  If you’re unfamiliar with the terms  and , see [`TN3137: On Mac keychain APIs and implementations`](tn3137-on-mac-keychains.md).

While the example above assumes you’re authenticating with an app-specific password, this technique also works with an App Store Connect API key.  See the `notarytool` help for the details.

##### Notarizing on a Limited System

The standard way to get `notarytool` is to install Xcode.  If you don’t want to install a full copy of Xcode on your system, get `notarytool` by installing the Command Line Tools package.  This installs the same `notarytool` as the associated Xcode.

There are two ways to install the package:

- On the target system, run `xcrun` with the `--install` option.
- Download it from the [`Developer > Downloads`](https://developer.apple.comhttps://developer.apple.com/download/) page.  To get a list of available packages, switch to the More tab at the top right and search for .

On some systems even the Command Line Tools package is too big.  In that case, it’s fine to extract `notarytool` from either Xcode or the Command Line Tools package and copy it to your system.  On a system that has one of these installed, use `xcrun` to find `notarytool` and then copy it to wherever you want:

```shell
% xcrun --find notarytool
/Applications/Xcode.app/Contents/Developer/usr/bin/notarytool
% cp /Applications/Xcode.app/Contents/Developer/usr/bin/notarytool …whereever…
```

##### Enable Notarization on an Older Version of Macos

The first version of Xcode to include `notarytool` is Xcode 13.  It requires macOS 11.3.  It is, however, possible to notarize on earlier systems, all the way back to macOS 10.15.  To do this, copy `notarytool` from a system with Xcode or the Command Line Tools package installed, as described in the previous section.

> ❗ **Important**: Apple engineered `notarytool` to work back to macOS 10.15 regardless of the minimum system version of the product in which it’s contained.  This is a special case and does not apply to any other component within Xcode.

##### Learn About Completed Submissions

If you notarize using `altool`, the notary service sends you an email when it’s done processing your submission.  It doesn’t do this when you notarize with `notarytool`.  If you were previously relying on this email to trigger events in your workflow, consider one of the following `submit` subcommand options:

- `--wait`, which waits for your submission to complete
- `--webhook`, which notifies you when your submission is complete

#### Revision History

-  Fixed a broken link.
-  Fixed a bug in the `--notarization-history` examples.  Made other minor editorial changes.
-  Updated to include the announced end date for `altool`.
-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3147-migrating-to-the-latest-notarization-tool)*