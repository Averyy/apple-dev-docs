# update()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates the underlying value of the stored value.

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
mutating func update()
```

## Discussion

SwiftUI calls this function before rendering a view’s [`body`](../view/body-8kl5o.md) to ensure the view has the most recent value.

## Default Implementations

### DynamicProperty Implementations
- [func update()](./update%28%29-9fxv4.md)
  Updates the underlying value of the stored value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicproperty/update())*