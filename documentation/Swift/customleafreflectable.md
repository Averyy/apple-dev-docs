# CustomLeafReflectable

**Framework**: Swift  
**Kind**: protocol

A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol CustomLeafReflectable : CustomReflectable
```

## Relationships

### Inherits From
- [CustomReflectable](customreflectable.md)

## See Also

- [protocol CustomReflectable](customreflectable.md)
  A type that explicitly supplies its own mirror.
- [protocol CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md)
  A type that supplies a custom description for playground logging.
- [typealias PlaygroundQuickLook](playgroundquicklook.md)
  The sum of types that can be used as a Quick Look representation.
- [macro DebugDescription()](debugdescription().md)
  Converts description definitions to a debugger Type Summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/customleafreflectable)*