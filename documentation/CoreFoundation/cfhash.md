# CFHash(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a code that can be used to identify an object in a hashing structure.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFHash(_ cf: CFTypeRef!) -> CFHashCode
```

#### Return Value

An integer of type [`CFHashCode`](cfhashcode.md) that represents a hashing value for `cf`.

#### Discussion

Two objects that are equal (as determined by the [`CFEqual(_:_:)`](cfequal(_:_:).md) function) have the same hashing value. However, the converse is not true: two objects with the same hashing value might not be equal. That is, hashing values are not necessarily unique.

The hashing value for an object might change from release to release or from platform to platform.

## Parameters

- `cf`: A CFType object to examine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfhash(_:))*