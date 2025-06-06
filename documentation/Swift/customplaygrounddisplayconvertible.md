# CustomPlaygroundDisplayConvertible

**Framework**: Swift  
**Kind**: protocol

A type that supplies a custom description for playground logging.

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
protocol CustomPlaygroundDisplayConvertible
```

#### Overview

Playground logging can generate, at a minimum, a structured description of any type. If you want to provide a custom description of your type to be logged in place of the default description, conform to the `CustomPlaygroundDisplayConvertible` protocol.

Playground logging generates a richer, more specialized description of core types. For example, the contents of a `String` are logged, as are the components of an `NSColor` or `UIColor`. The current playground logging implementation logs specialized descriptions of at least the following types:

- `String` and `NSString`
- `Int`, `UInt`, and the other standard library integer types
- `Float` and `Double`
- `Bool`
- `Date` and `NSDate`
- `NSAttributedString`
- `NSNumber`
- `NSRange`
- `URL` and `NSURL`
- `CGPoint`, `CGSize`, and `CGRect`
- `NSColor`, `UIColor`, `CGColor`, and `CIColor`
- `NSImage`, `UIImage`, `CGImage`, and `CIImage`
- `NSBezierPath` and `UIBezierPath`
- `NSView` and `UIView`

Playground logging may also be able to support specialized descriptions of other types.

#### Conforming to the Customplaygrounddisplayconvertible Protocol

To add `CustomPlaygroundDisplayConvertible` conformance to your custom type, implement the `playgroundDescription` property. If your implementation returns an instance of one of the types above, that type’s specialized description is used. If you return any other type, a structured description is generated.

If your type has value semantics, the `playgroundDescription` should be unaffected by subsequent mutations, if possible.

If your type’s `playgroundDescription` returns an instance which itself conforms to `CustomPlaygroundDisplayConvertible`, then that type’s `playgroundDescription` will be used, and so on. To prevent infinite loops, playground logging implementations can place a reasonable limit on this kind of chaining.

## Topics

### Instance Properties
- [var playgroundDescription: Any](customplaygrounddisplayconvertible/playgrounddescription.md)
  A custom playground description for this instance.

## See Also

- [protocol CustomReflectable](customreflectable.md)
  A type that explicitly supplies its own mirror.
- [protocol CustomLeafReflectable](customleafreflectable.md)
  A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.
- [typealias PlaygroundQuickLook](playgroundquicklook.md)
  The sum of types that can be used as a Quick Look representation.
- [macro DebugDescription()](debugdescription().md)
  Converts description definitions to a debugger Type Summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/customplaygrounddisplayconvertible)*