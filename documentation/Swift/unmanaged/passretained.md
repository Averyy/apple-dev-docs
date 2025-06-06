# passRetained(_:)

**Framework**: Swift  
**Kind**: method

Creates an unmanaged reference with an unbalanced retain.

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
static func passRetained(_ value: Instance) -> Unmanaged<Instance>
```

#### Return Value

An unmanaged reference to the object passed as `value`.

#### Discussion

The instance passed as `value` will leak if nothing eventually balances the retain.

This is useful when passing an object to an API which Swift does not know the ownership rules for, but you know that the API expects you to pass the object at +1.

## Parameters

- `value`: A class instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged/passretained(_:))*