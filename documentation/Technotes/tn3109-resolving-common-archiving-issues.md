# TN3109: Resolving common archiving issues

**Framework**: Technotes

Handle common issues that arise while archiving apps.

#### Overview

When you choose Product > Archive, Xcode creates an archive of your app that will appear in the Archives organizer. If the Archives organizer reports your archive as an app archive, then you can validate or distribute it.

#### The Archive Command in the Product Menu Is Disabled

You can choose Product > Archive in Xcode after meeting these requirements:

- You’ve selected a real device or build-only device as the run destination in the scheme building your app. Apps built with simulator SDKs can’t be archived nor submitted to the App Store; see [`Running Your App in the Simulator or on a Device`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/running-your-app-in-the-simulator-or-on-a-device).
- You’ve enabled the archive action for the scheme building your app. ![Select archive in the scheme editor.](/images/com.apple.technotes/tn3109-archive_selected@2x.png)

#### Xcode Successfully Archived My App But the Archive Doesnt Appear in the Archives Organizer

Archives appear in the Archives organizer when meeting these requirements:

- Your archive is an app archive. If the Archives organizer reports your archive as generic, read [`TN3110: Resolving generic Xcode archive issue`](tn3110-resolving-generic-xcode-archive-issue.md).
- You’ve selected the `Reveal Archive in Organizer` option in the archive action for the scheme building your app. ![Select Reveal Archive in Organizer in the scheme editor.](/images/com.apple.technotes/tn3109-reveal_archive_in_organizer@2x.png)

#### The Validate Content Button Is Disabled

You have a generic Xcode archive. The Validate Content button is enabled for app archives and disabled for generic ones. ![The Validate Content button is disabled.](/images/com.apple.technotes/tn3109-validate_content_disabled@2x.png) See [`TN3110: Resolving generic Xcode archive issue`](tn3110-resolving-generic-xcode-archive-issue.md) for details.

#### Unexpected Build Products and Archive Methods in the Archive Organizer When Attempting to Distribute My Archive

If the Archives organizer offers to distribute your archive’s built product or to export a copy of it, then your archive is likely a generic one. ![Select Built Products or Archive in the Archives organizer.](/images/com.apple.technotes/tn3109-select_distribution_method@2x.png) Read [`TN3110: Resolving generic Xcode archive issue`](tn3110-resolving-generic-xcode-archive-issue.md) for information on how to resolve it.

#### Revision History

- **2022-05-24** Made minor editorial changes.
- **2022-02-08** Republished as TN3109 with significant editorial changes.
- **2015-10-15** Updated for Xcode 7.
- **2015-10-14** Updated for Xcode 7.
- **2015-08-18** Made editorial changes.
- **2015-03-27** Updated for Xcode 6.
- **2014-07-17** Fixed typos.
- **2014-03-17** Updated the “Unexpected Save Built Products and Export as Xcode Archive options in the Archives Organizer when attempting to distribute my archive” section.
- **2012-06-28** Added information on how to resolve the Archives Organizer’s “Save Built Products” and “Export as Xcode Archive” issue.
- **2011-09-12** First published as TN2215.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3109-resolving-common-archiving-issues)*