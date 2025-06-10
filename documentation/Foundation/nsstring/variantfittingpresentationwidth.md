# variantFittingPresentationWidth(_:)

**Framework**: Foundation  
**Kind**: method

Returns a string variation suitable for the specified presentation width.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func variantFittingPresentationWidth(_ width: Int) -> String
```

#### Return Value

A string variation, or the original string if no variations exist for the specified width.

#### Discussion

You can use this method to provide adaptive strings for the user’s device—that is, text that avoids truncation and maximizes available space. For example, an app running on an iPad Pro in Landscape orientation might welcome a user with the message “Greetings and Salutations!”, whereas the same app running on an iPhone SE in Portrait orientation might instead show an abbreviated welcome message, like “Hello!”.

> **Note**:  Don’t call this method when setting user-visible text for standard UIKit controls, such as [`UILabel`](https://developer.apple.com/documentation/UIKit/UILabel). UIKit provides built-in support for adaptive strings, and automatically selects the string width variant appropriate for the current screen size according to the behavior described below.

Call this method on a string with one or more width variations. You define width variations for a localized string in a Stringsdict file using the `NSStringVariableWidthRuleType` key, and then retrieve a string with variations using [`NSLocalizedString`](nslocalizedstring.md).

For example, consider the `stringsdict.plist` file in the first listing and the corresponding code in the second listing.

```other
<plist version="1.0"><key>hello</key>
<dict>
    <key>NSStringVariableWidthRuleType</key>
    <dict>
        <key>1</key>
        <string>Hi!</string>
        <key>20</key>
        <string>Hello!</string>
        <key>70</key>
        <string>Greetings and Salutations!</string>
    </dict>
</dict>
```

```swift
let adaptiveString = NSLocalizedString("hello")

print(adaptiveString.variantFittingPresentationWidth(10)) // Prints "Hi!"
print(adaptiveString.variantFittingPresentationWidth(25)) // Prints "Hello!"
print(adaptiveString.variantFittingPresentationWidth(70)) // Prints "Greetings and Salutations!"
```

##### Understanding How Width Variants Are Selected

This method selects a variation for a specified width according to the following behavior:

- If no variations exist for the string, the original string is returned.
- If a variation exists for the specified width, that string is returned.
- If no variation is found with a width less than the specified value, the variation with the smallest width is returned.
- Otherwise, the variation with the next smallest width value is returned.

##### Specifying Width Values

Smaller width values correspond to shorter strings, whereas larger values correspond to longer strings. By default, width values do not have an associated unit.

In iOS, width contexts are measured by the number of em units that fit across the app window. This value depends on several factors, including the size and orientation of the device, the user’s preferred content size category, whether the Zoom accessibility feature is enabled, and whether the app is displayed in a multitasking context, such as in Split View or Slide Over.

## Parameters

- `width`: The desired width of the string variation.

## See Also

- [func draw(at: CGPoint, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(at:withattributes:).md)
  Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [func draw(in: CGRect, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(in:withattributes:).md)
  Draws the attributed string inside the specified bounding rectangle.
- [func draw(with: CGRect, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?)](nsstring/draw(with:options:attributes:context:).md)
  Draws the attributed string in the specified bounding rectangle using the provided options.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?) -> CGRect](nsstring/boundingrect(with:options:attributes:context:).md)
  Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](nsstring/size(withattributes:).md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [struct NSStringDrawingOptions](../UIKit/NSStringDrawingOptions.md)
  Constants that specify the rendering options for drawing a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/variantfittingpresentationwidth(_:))*