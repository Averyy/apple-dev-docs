# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets the value of the specified key to a property list object.

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
func set(_ value: Any?, forKey defaultName: String)
```

#### Discussion

Use this method to write property list object types to the defaults store. To store types that aren’t property list objects, archive them to a [`Data`](data.md) object and use this method to save that data object to the defaults store.

After you call this method, the system generates a [`didChangeNotification`](userdefaults/didchangenotification.md) for registered observers.

## Parameters

- `value`: The property-list type to store in the defaults database. If you specify an   array or dictionary type, those collections must similarly contain only property list types.
- `defaultName`: The key that contains the setting’s name.

## See Also

- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified key to a Boolean value.
- [func set(Int, forKey: String)](userdefaults/set(_:forkey:)-3v852.md)
  Sets the value of the specified key to an integer.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified key to a floating-point number.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified key to a double.
- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified key to a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-8ab6d)*