# init(configuration:primaryAction:)

**Framework**: UIKit  
**Kind**: init

Creates a new button with the specified configuration and registers the primary action event.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(configuration: UIButton.Configuration, primaryAction: UIAction? = nil)
```

#### Discussion

If the primary action contains a title or an image, this method copies them to the configuration and the button displays them.

## Parameters

- `configuration`: The button configuration.
- `primaryAction`: The action to perform for the   control event.

## See Also

- [UIButton.Configuration](uibutton/configuration-swift.struct.md)
  A configuration that specifies the appearance and behavior of a button and its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/init(configuration:primaryaction:))*