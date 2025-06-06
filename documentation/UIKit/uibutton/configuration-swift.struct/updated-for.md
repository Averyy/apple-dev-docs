# updated(for:)

**Framework**: UIKit  
**Kind**: method

Returns a copy of the configuration, updated for the given button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
func updated(for button: UIButton) -> UIButton.Configuration
```

#### Return Value

An updated configuration. This method preserves custom values set on the configuration, and updates default values based on the button state.

## Parameters

- `button`: A button to use as a basis for the configuration.

## See Also

- [static func plain() -> UIButton.Configuration](uibutton/configuration-swift.struct/plain.md)
  Creates a configuration for a button with a transparent background.
- [static func gray() -> UIButton.Configuration](uibutton/configuration-swift.struct/gray.md)
  Creates a configuration for a button with a gray background.
- [static func tinted() -> UIButton.Configuration](uibutton/configuration-swift.struct/tinted.md)
  Creates a configuration for a button with a tinted background color.
- [static func filled() -> UIButton.Configuration](uibutton/configuration-swift.struct/filled.md)
  Creates a configuration for a button with a background filled with the button’s tint color.
- [static func borderless() -> UIButton.Configuration](uibutton/configuration-swift.struct/borderless.md)
  Creates a configuration for a button that has a borderless style.
- [static func bordered() -> UIButton.Configuration](uibutton/configuration-swift.struct/bordered.md)
  Creates a configuration for a button that has a bordered style.
- [static func borderedTinted() -> UIButton.Configuration](uibutton/configuration-swift.struct/borderedtinted.md)
  Creates a configuration for a button that has a tinted, bordered style.
- [static func borderedProminent() -> UIButton.Configuration](uibutton/configuration-swift.struct/borderedprominent.md)
  Creates a configuration for a button that has a prominent, bordered style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/updated(for:))*