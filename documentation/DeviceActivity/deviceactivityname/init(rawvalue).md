# init(rawValue:)

**Framework**: Device Activity  
**Kind**: init  
**Role**: Initializer

Creates a new instance with the specified raw value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

The following code example prints the specified raw value.

```swift
extension DeviceActivityName {
    static let bedtime = Self("Bedtime")
}

print(DeviceActivityName.bedtime.rawValue)
// Prints "Bedtime".
```

## Parameters

- `rawValue`: The raw value to use for the new instance.

## See Also

### Creating an Instance
- [init(String)](./init%28_%29.md)
  Creates a new instance with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityname/init(rawvalue:))*