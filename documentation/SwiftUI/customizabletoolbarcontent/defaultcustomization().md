# defaultCustomization()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures customizable toolbar content with the default visibility and options.

**Availability**:
- iOS 16.0+ - Deprecated in 16.0
- iPadOS 16.0+ - Deprecated in 16.0
- Mac Catalyst 16.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 13.0
- tvOS 16.0+ - Deprecated in 16.0
- visionOS 1.0+
- watchOS 9.0+ - Deprecated in 9.0

> **Deprecated**: Please provide either a visibility or customization options

## Declaration

```swift
func defaultCustomization() -> some CustomizableToolbarContent
```

#### Discussion

Use the [`defaultCustomization(_:options:)`](./defaultcustomization%28_,options%29.md) modifier providing either a `defaultVisibility` or `options` instead.

## See Also

### Using default options
- [func defaultCustomization(Visibility, options: ToolbarCustomizationOptions) -> some CustomizableToolbarContent](./defaultcustomization%28_,options%29.md)
  Configures the way customizable toolbar items with the default behavior behave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/defaultcustomization())*