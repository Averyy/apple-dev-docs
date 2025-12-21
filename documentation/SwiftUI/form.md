# Form

**Framework**: SwiftUI  
**Kind**: struct

A container for grouping controls used for data entry, such as in settings or inspectors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Form<Content> where Content : View
```

## Mentions

- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)

#### Overview

SwiftUI applies platform-appropriate styling to views contained inside a form, to group them together. Form-specific styling applies to things like buttons, toggles, labels, lists, and more. Keep in mind that these stylings may be platform-specific. For example, forms appear as grouped lists on iOS, and as aligned vertical stacks on macOS.

The following example shows a simple data entry form on iOS, grouped into two sections. The supporting types (`NotifyMeAboutType` and `ProfileImageSize`) and state variables (`notifyMeAbout`, `profileImageSize`, `playNotificationSounds`, and `sendReadReceipts`) are omitted for simplicity.

```swift
var body: some View {
    NavigationView {
        Form {
            Section(header: Text("Notifications")) {
                Picker("Notify Me About", selection: $notifyMeAbout) {
                    Text("Direct Messages").tag(NotifyMeAboutType.directMessages)
                    Text("Mentions").tag(NotifyMeAboutType.mentions)
                    Text("Anything").tag(NotifyMeAboutType.anything)
                }
                Toggle("Play notification sounds", isOn: $playNotificationSounds)
                Toggle("Send read receipts", isOn: $sendReadReceipts)
            }
            Section(header: Text("User Profiles")) {
                Picker("Profile Image Size", selection: $profileImageSize) {
                    Text("Large").tag(ProfileImageSize.large)
                    Text("Medium").tag(ProfileImageSize.medium)
                    Text("Small").tag(ProfileImageSize.small)
                }
                Button("Clear Image Cache") {}
            }
        }
    }
}
```

![A form on iOS, presented as a grouped list with two sections. The](https://docs-assets.developer.apple.com/published/9b9f14a16c5d9d1fed7b121071bdb262/SwiftUI-Form-iOS%402x.png)

On macOS, a similar form renders as a vertical stack. To adhere to macOS platform conventions, this version doesn’t use sections, and uses colons at the end of its labels. It also sets the picker to use the [`inline`](pickerstyle/inline.md) style, which produces radio buttons on macOS.

```swift
var body: some View {
    Spacer()
    HStack {
        Spacer()
        Form {
            Picker("Notify Me About:", selection: $notifyMeAbout) {
                Text("Direct Messages").tag(NotifyMeAboutType.directMessages)
                Text("Mentions").tag(NotifyMeAboutType.mentions)
                Text("Anything").tag(NotifyMeAboutType.anything)
            }
            Toggle("Play notification sounds", isOn: $playNotificationSounds)
            Toggle("Send read receipts", isOn: $sendReadReceipts)

            Picker("Profile Image Size:", selection: $profileImageSize) {
                Text("Large").tag(ProfileImageSize.large)
                Text("Medium").tag(ProfileImageSize.medium)
                Text("Small").tag(ProfileImageSize.small)
            }
            .pickerStyle(.inline)

            Button("Clear Image Cache") {}
        }
        Spacer()
    }
    Spacer()
}
```

![A form on iOS, presented as a vertical stack of views. At top, it shows](https://docs-assets.developer.apple.com/published/cdbe25e36916e95c7d68402249d02bb4/SwiftUI-Form-macOS%402x.png)

## Topics

### Creating a form
- [init(content: () -> Content)](form/init(content:).md)
  Creates a form with the provided content.
### Creating a form from a configuration
- [init(FormStyleConfiguration)](form/init(_:).md)
  Creates a form based on a form style configuration.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [struct LabeledContent](labeledcontent.md)
  A container for attaching a label to a value-bearing view.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/form)*