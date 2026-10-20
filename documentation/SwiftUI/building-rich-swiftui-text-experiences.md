# Building rich SwiftUI text experiences

**Framework**: SwiftUI  
**Role**: Sample Code  
**Download**: [BuildingRichSwiftUITextExperiences.zip](https://docs-assets.developer.apple.com/published/af5124237a05/BuildingRichSwiftUITextExperiences.zip)

Build an editor for formatted text using SwiftUI text editor views and attributed strings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- Xcode 26.0+

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 280: [Code-along: Cook up a rich text experience in SwiftUI with AttributedString](https://developer.apple.com/wwdc25/280/).

You can follow along with the code written in the WWDC25 session, learning how to upgrade `TextEditor` to rich text, build custom controls, and constrain the formatting options the editor provides.

After the code-along, you can learn more about how to persist rich text using SwiftData, and how to export rich text documents using the `Transferable` protocol.

##### Configure the sample code project

To configure the sample code project, do the following in Xcode:

1. Open the sample with the latest version of Xcode.
2. Set the developer team to let Xcode automatically manage the provisioning profile. For more information, see [Set the bundle ID](../Xcode/preparing-your-app-for-distribution.md) and [Assign the project to a team](../Xcode/preparing-your-app-for-distribution.md).

## See Also

### Getting text input
- [struct TextField](./textfield.md)
  A control that displays an editable text interface.
- [func textFieldStyle<S>(S) -> some View](./view/textfieldstyle%28_%29.md)
  Sets the style for text fields within this view.
- [struct SecureField](./securefield.md)
  A control into which people securely enter private text.
- [struct TextEditor](./texteditor.md)
  A view that can display and edit long-form text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/building-rich-swiftui-text-experiences)*