# rawValue

**Framework**: DeviceActivity  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var rawValue: String
```

#### Discussion

A new instance initialized with `rawValue` prints the specified raw value. For example:

```swift
extension DeviceActivityName {
    static let bedtime = Self("Bedtime")
}

print(DeviceActivityName.bedtime.rawValue)
// Prints "Bedtime".
```

## See Also

- [init(rawValue: String)](deviceactivityname/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init(String)](deviceactivityname/init(_:).md)
  Creates a new instance with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityname/rawvalue-swift.property)*