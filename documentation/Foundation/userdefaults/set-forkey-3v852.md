# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets the value of the specified key to an integer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func set(_ value: Int, forKey defaultName: String)
```

#### Discussion

This method places the integer value in an [`NSNumber`](nsnumber.md) type before writing the key and value to the defaults database. After you call this method, the system generates a [`didChangeNotification`](userdefaults/didchangenotification.md) for registered observers.

## Parameters

- `value`: The integer value to store in the defaults database.
- `defaultName`: The key that contains the setting’s name.

## See Also

- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified key to a Boolean value.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified key to a floating-point number.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified key to a double.
- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified key to a URL.
- [func set(Any?, forKey: String)](userdefaults/set(_:forkey:)-8ab6d.md)
  Sets the value of the specified key to a property list object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-3v852)*