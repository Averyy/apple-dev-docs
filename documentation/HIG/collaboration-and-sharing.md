---
url: https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing
framework: HIG
---

# Collaboration and sharing

**Type:** article

**Platforms:** ios, ipados, macos, visionos, watchos

> **Updated 2023-12-05:** Added artwork illustrating button placement and various types of collaboration permissions.

Great collaboration and sharing experiences are simple and responsive, letting people engage with the content while communicating effectively with others.

![A sketch of a person with an overlapping checkmark, suggesting effective collaboration. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/15e8e897799df1e35f84c109cf8c20ef/patterns-collaboration-and-sharing-intro~dark%402x.png)
System interfaces and the Messages app can help you provide consistent and convenient ways for people to collaborate and share. For example, people can share content or begin a collaboration by dropping a document into a Messages conversation or selecting a destination in the familiar share sheet.
After a collaboration begins, people can use the Collaboration button in your app to communicate with others, perform custom actions, and manage details. In addition, people can receive Messages notifications when collaborators mention them, make changes, join, or leave.
You can take advantage of Messages integration and the system-provided sharing interfaces whether you implement collaboration and sharing through CloudKit, iCloud Drive, or a custom solution. To offer these features when you use a custom collaboration infrastructure, make sure your app also supports universal links (for developer guidance, see [Supporting universal links in your app](../Xcode/supporting-universal-links-in-your-app.md)).
In addition to helping people share and collaborate on documents, visionOS supports immersive sharing experiences through SharePlay. For guidance, see [SharePlay](shareplay.md).

## Best practices
**Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating.** In iOS 16, the system-provided share sheet includes ways to choose a file-sharing method and set permissions for a new collaboration; iPadOS 16 and macOS 13 introduce similar appearance and functionality in the sharing popover. In your SwiftUI app, you can also enable sharing by presenting a share link that opens the system-provided share sheet when people choose it; for developer guidance, see [ShareLink](../SwiftUI/ShareLink.md).
![An illustration of a Notes document on iPhone. The document toolbar prominently features the Share button next to the More button.](https://docs-assets.developer.apple.com/published/ad076657b4b7d970bd92ebab2db77ae6/collaboration-share-button~dark%402x.png)
**If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports.** If you use CloudKit, you can add support for sending a copy of a file by passing both the file and your collaboration object to the share sheet. Because the share sheet has built-in support for multiple items, it automatically detects the file and makes the “send copy” functionality available. With iCloud Drive, your collaboration object supports “send copy” functionality by default. For custom collaboration, you can support “send copy” functionality in the share sheet by including a file — or a plain text representation of it — in your collaboration object.
**Write succinct phrases that summarize the sharing permissions you support.** For example, you might write phrases like “Only invited people can edit” or “Everyone can make changes.” The system uses your permission summary in a button that reveals a set of sharing options that people use to define the collaboration.
![An illustration of a Notes document with the share sheet open on iPhone, with collaboration options set to indicate that only invited people can edit the selected document.](https://docs-assets.developer.apple.com/published/139f364cca53aa734f96374a4a9163cc/collaboration-sharing-permission-invited~dark%402x.png)
![An illustration of a Notes document with the share sheet open on iPhone, with collaboration options set to indicate that everyone can make changes to the selected document.](https://docs-assets.developer.apple.com/published/42e8af3f8ba0ce30aa46315f6771ec67/collaboration-sharing-permission-everyone~dark%402x.png)
**Provide a set of simple sharing options that streamline collaboration setup.** You can customize the view that appears when people choose the permission summary button to provide choices that reflect your collaboration functionality. For example, you might offer options that let people specify who can access the content and whether they can edit it or just read it, and whether collaborators can add new participants. Keep the number of custom choices to a minimum and group them in ways that help people understand them at a glance.
**Prominently display the Collaboration button as soon as collaboration starts.** The system-provided Collaboration button reminds people that the content is shared and identifies who’s sharing it. Because the Collaboration button typically appears after people interact with the share sheet or sharing popover, it works well to place it next to the Share button.
![An illustration of a Notes document open on iPhone. The document toolbar prominently features the Collaboration button next to the Share button.](https://docs-assets.developer.apple.com/published/833bd8ed783da16a60a5d542108c5d38/collaboration-status-active-collaboration-button~dark%402x.png)
**Provide custom actions in the collaboration popover only if needed.** Choosing the Collaboration button in your app reveals a popover that consists of three sections. The top section lists collaborators and provides communication buttons that can open Messages or FaceTime, the middle section contains your custom items, and the bottom section displays a button people use to manage the shared file. You don’t want to overwhelm people with too much information, so it’s crucial to offer only the most essential items that people need while they use your app to collaborate. For example, Notes summarizes the most recent updates and provides buttons that let people get more information about the updates or view more activities.
![An illustration of a Notes document on iPhone. A menu is open from the Collaboration button in the document toolbar, with buttons to display the most recent updates and activities.](https://docs-assets.developer.apple.com/published/e76d8c06da7717e95ba05bcfe65d22e8/collaboration-custom-popover-notes~dark%402x.png)
**If it makes sense in your app, customize the title of the modal view’s collaboration-management button.** People choose this button — titled “Manage Shared File” by default — to reveal the collaboration-management view where they can change settings and add or remove collaborators. If you use CloudKit sharing, the system provides a management view for you; otherwise, you create your own.
**Consider posting collaboration event notifications in Messages.** Choose the type of event that occurred — such as a change in the content or the collaboration membership, or the mention of a participant — and include a universal link people can use to open the relevant view in your app. For developer guidance, see [SWHighlightEvent](../SharedWithYou/SWHighlightEvent.md).

## Platform considerations
*No additional considerations for iOS, iPadOS, or macOS. Not available in tvOS.*

### visionOS
By default, the system supports screen sharing for an app running in the Shared Space by streaming the current window to other collaborators. If one person transitions the app to a Full Space while sharing is in progress, the system pauses the stream for other people until the app returns to the Shared Space. For guidance, see [Immersive experiences](immersive-experiences.md).

### watchOS
In your SwiftUI app running in watchOS, use [ShareLink](../SwiftUI/ShareLink.md) to present the system-provided share sheet.

## Resources

#### Related
[Activity views](activity-views.md)

#### Developer documentation
[Shared with You](../SharedWithYou.md)
[ShareLink](../SwiftUI/ShareLink.md) — SwiftUI

#### Videos
- [Design for Collaboration with Messages](https://developer.apple.com/videos/play/wwdc2022/10015) - Discover how you can design great collaboration experiences using Apple platforms. We’ll show you how to combine the Share Sheet, live editing notifications, Messages, FaceTime, and your app’s existing collaboration features to help people connect and collaborate effortlessly.
- [Enhance collaboration experiences with Messages](https://developer.apple.com/videos/play/wwdc2022/10095) - Discover how you can help improve communication and collaboration in your app with Collaboration in Messages. Learn how to tie a document to Messages conversations for simple sharing and discussion. Explore how you can keep everyone in the conversation up to date on the latest activity in the document. And find out how you can add customizable UI in your app to manage collaboration details and connect documents to Messages conversations and FaceTime calls. 

To learn more about the SharedWithYou framework, we recommend watching "Add Shared with You to your app.” For more information on adding collaboration APIs to apps that have custom collaboration infrastructure, check out "Integrate your custom collaboration app with Messages.”
- [Integrate your custom collaboration app with Messages](https://developer.apple.com/videos/play/wwdc2022/10093) - Discover how the SharedWithYou framework can augment your app's collaboration infrastructure. We'll show you how to send secure invitations to collaborative content and synchronize participant changes. We'll also cover displaying content updates within the relevant conversation.

For an introduction to SharedWithYou, watch "Add Shared with You to your app" from WWDC22. For an overview of the collaboration UI APIs, watch "Enhance collaboration experiences with Messages" from WWDC22.

## Change log
| Date | Changes |
| --- | --- |
| December 5, 2023 | Added artwork illustrating button placement and various types of collaboration permissions. |
| June 21, 2023 | Updated to include guidance for visionOS. |
| September 14, 2022 | New page. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing)*
