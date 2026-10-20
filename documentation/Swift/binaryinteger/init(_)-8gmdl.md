# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Creates a new instance from the given integer.

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
init<T>(_ source: T) where T : BinaryInteger
```

#### Discussion

If the value passed as `source` is not representable in this type, a runtime error may occur.

```swift
let x = -500 as Int
let y = Int32(x)
// y == -500

// -500 is not representable as a 'UInt32' instance
let z = UInt32(x)
// Error
```

## Parameters

- `source`: An integer to convert. `source` must be representable in this type.

## Default Implementations

### BinaryInteger Implementations
- [init?(String)](./init%28_%29-3cx61.md)
  Creates a new integer value from the given string.
- [init<T>(T)](./init%28_%29-5yrn0.md)
  Creates a new instance from the given integer.
- [init<T>(T)](./init%28_%29-62cdc.md)
- [init<T>(T)](./init%28_%29-6u4mr.md)
  Creates a new instance from the given integer.
### FixedWidthInteger Implementations
- [init?(Backtrace.Address)](../fixedwidthinteger/init%28_%29.md)
  Convert from an Backtrace.Address.

## See Also

### Converting Integers
- [init<T>(clamping: T)](./init%28clamping%29.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](./init%28truncatingifneeded%29.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/init(_:)-8gmdl)*