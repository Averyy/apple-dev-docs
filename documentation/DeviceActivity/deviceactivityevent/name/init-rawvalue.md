# init(rawValue:)

**Framework**: DeviceActivity  
**Kind**: init

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
extension DeviceActivityEvent.Name {
    static let event = Self("Event")
}

print(DeviceActivityEvent.Name.event.rawValue)
// Prints "Event".
```

## Parameters

- `rawValue`: The raw value to use for the new instance.

## See Also

- [init(String)](deviceactivityevent/name/init(_:).md)
  Creates a new instance with the specified raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name/init(rawvalue:))*