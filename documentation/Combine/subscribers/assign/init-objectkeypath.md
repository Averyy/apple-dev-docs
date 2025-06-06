# init(object:keyPath:)

**Framework**: Combine  
**Kind**: init

Creates a subscriber to assign the value of a property indicated by a key path.

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
init(object: Root, keyPath: ReferenceWritableKeyPath<Root, Input>)
```

## Parameters

- `object`: The object that contains the property. The subscriber assigns the object’s property every time it receives a new value.
- `keyPath`: A key path that indicates the property to assign. See   in   to learn how to use key paths to specify a property of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign/init(object:keypath:))*