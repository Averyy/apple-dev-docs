---
url: https://developer.apple.com/design/human-interface-guidelines/action-sheets
framework: HIG
---

# Action sheets

**Type:** article

**Platforms:** ios, ipados, macos, tvos, watchos

An action sheet is a modal view that presents choices related to an action people initiate.

![A stylized representation of a set of action sheet buttons at the bottom of an iPhone. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/fc0b086137604dbce2701ce7532ddfca/components-action-sheet-intro~dark%402x.png)

> **Note:** When you use SwiftUI, you can offer action sheet functionality in all platforms by specifying a [presentation modifier](https://developer.apple.com/documentation/swiftui/view-presentation) for a confirmation dialog. If you use UIKit, you use the [UIAlertController.Style.actionSheet](../UIKit/UIAlertController/Style/actionSheet.md) to display an action sheet in iOS, iPadOS, and tvOS.

## Best practices
**Use an action sheet — not an alert — to offer choices related to an intentional action.** For example, when people cancel the message they’re editing in Mail on iPhone, an action sheet provides two choices: delete the draft, or save the draft. Although an alert can also help people confirm or cancel an action that has destructive consequences, it doesn’t provide additional choices related to the action. More importantly, an alert is usually unexpected, generally telling people about a problem or a change in the current situation that might require them to act. For guidance, see [Alerts](alerts.md).
![A partial screenshot of a new message being composed in Mail on iPhone.](https://docs-assets.developer.apple.com/published/cfa0d84cf04367441dbe47bc0934de46/action-sheet-iphone-mail~dark%402x.png)
![A partial screenshot of a new message being composed in Mail on iPhone, with the action sheet open after choosing to cancel the message. The action sheet presents choices to delete the draft or save the draft.](https://docs-assets.developer.apple.com/published/ba31ffab2e8cfb31594c7dc204a64f4a/action-sheet-iphone-mail-delete-action~dark%402x.png)
**Use action sheets sparingly.** Action sheets give people important information and choices, but they interrupt the current task to do so. To encourage people to pay attention to action sheets, avoid using them more than necessary.
**Aim to keep titles short enough to display on a single line.** A long title is difficult to read quickly and might get truncated or require people to scroll.
**Provide a message only if necessary.** In general, the title — combined with the context of the current action — provides enough information to help people understand their choices.
**If necessary, provide a Cancel button that lets people reject an action that might destroy data.** Place the Cancel button at the bottom of the action sheet (or in the upper-left corner of the sheet in watchOS). A SwiftUI confirmation dialog includes a Cancel button by default.
**Make destructive choices visually prominent.** Use the destructive style for buttons that perform destructive actions, and place these buttons at the top of the action sheet where they tend to be most noticeable. For developer guidance, see [destructive](../SwiftUI/ButtonRole/destructive.md) (SwiftUI) or [UIAlertAction.Style.destructive](../UIKit/UIAlertAction/Style-swift.enum/destructive.md) (UIKit).

## Platform considerations
*No additional considerations for macOS or tvOS. Not supported in visionOS.*

### iOS, iPadOS
**Use an action sheet — not a menu — to provide choices related to an action.** People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.
**Avoid letting an action sheet scroll.** The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.

### watchOS
The system-defined style for action sheets includes a title, an optional message, a Cancel button, and one or more additional buttons. The appearance of this interface is different depending on the device.
![An illustration of an action sheet on Apple Watch, showing content that represents text in the top half of the watch screen and two stacked buttons in the bottom half.](https://docs-assets.developer.apple.com/published/4ec6a46689c0ec4550d6fe48d4aa27a8/action-sheet-watch-system-defined%402x.png)
Each button has an associated style that conveys information about the button’s effect. There are three system-defined button styles:
| Style | Meaning |
| --- | --- |
| Default | The button has no special meaning. |
| Destructive | The button destroys user data or performs a destructive action in the app. |
| Cancel | The button dismisses the view without taking any action. |

**Avoid displaying more than four buttons in an action sheet, including the Cancel button.** When there are fewer buttons onscreen, it’s easier for people to view all their options at once. Because the Cancel button is required, aim to provide no more than three additional choices.

## Resources

#### Related
[Modality](modality.md)
[Sheets](sheets.md)
[Alerts](alerts.md)

#### Developer documentation
[confirmationDialog(_:isPresented:titleVisibility:actions:)](../SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:actions:)-46zbb.md) — SwiftUI
[UIAlertController.Style.actionSheet](../UIKit/UIAlertController/Style/actionSheet.md) — UIKit



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/action-sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)*
