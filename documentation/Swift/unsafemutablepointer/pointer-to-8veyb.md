# pointer(to:)

**Framework**: Swift  
**Kind**: method

Obtain a mutable pointer to the stored property referred to by a key path.

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
func pointer<Property>(to property: WritableKeyPath<Pointee, Property>) -> UnsafeMutablePointer<Property>?
```

#### Return Value

A mutable pointer to the stored property represented by the key path, or `nil`.

#### Discussion

If the key path represents a computed property, this function will return `nil`.

## Parameters

- `property`: A   whose   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/pointer(to:)-8veyb)*