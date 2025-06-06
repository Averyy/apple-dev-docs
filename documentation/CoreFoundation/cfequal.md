# CFEqual(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Determines whether two Core Foundation objects are considered equal.

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
func CFEqual(_ cf1: CFTypeRef!, _ cf2: CFTypeRef!) -> Bool
```

#### Return Value

`true` if `cf1` and `cf2` are of the same type and considered equal, otherwise `false`.

#### Discussion

Equality is something specific to each Core Foundation opaque type. For example, two CFNumber objects are equal if the numeric values they represent are equal. Two CFString objects are equal if they represent identical sequences of characters, regardless of encoding.

## Parameters

- `cf1`: A CFType object to compare to  .
- `cf2`: A CFType object to compare to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfequal(_:_:))*