# updated(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a copy of the configuration, updated for the given button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
func updated(for button: UIButton) -> UIButton.Configuration
```

#### Return Value

An updated configuration. This method preserves custom values set on the configuration, and updates default values based on the button state.

## Parameters

- `button`: A button to use as a basis for the configuration.

## See Also

### Creating configurations
- [static func plain() -> UIButton.Configuration](./plain%28%29.md)
  Creates a configuration for a button with a transparent background.
- [static func gray() -> UIButton.Configuration](./gray%28%29.md)
  Creates a configuration for a button with a gray background.
- [static func tinted() -> UIButton.Configuration](./tinted%28%29.md)
  Creates a configuration for a button with a tinted background color.
- [static func filled() -> UIButton.Configuration](./filled%28%29.md)
  Creates a configuration for a button with a background filled with the button’s tint color.
- [static func borderless() -> UIButton.Configuration](./borderless%28%29.md)
  Creates a configuration for a button that has a borderless style.
- [static func bordered() -> UIButton.Configuration](./bordered%28%29.md)
  Creates a configuration for a button that has a bordered style.
- [static func borderedTinted() -> UIButton.Configuration](./borderedtinted%28%29.md)
  Creates a configuration for a button that has a tinted, bordered style.
- [static func borderedProminent() -> UIButton.Configuration](./borderedprominent%28%29.md)
  Creates a configuration for a button that has a prominent, bordered style.
- [static func glass() -> UIButton.Configuration](./glass%28%29.md)
  Creates a configuration for a button that has a Liquid Glass style.
- [static func prominentGlass() -> UIButton.Configuration](./prominentglass%28%29.md)
  Creates a configuration for a button that has a prominent Liquid Glass style.
- [static func clearGlass() -> UIButton.Configuration](./clearglass%28%29.md)
  Creates a configuration for a button that has a clear Liquid Glass style.
- [static func prominentClearGlass() -> UIButton.Configuration](./prominentclearglass%28%29.md)
  Creates a configuration for a button that has a prominent, clear Liquid Glass style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/updated(for:))*