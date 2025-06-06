# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets the value of the specified default key to the specified integer value.

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

This is a convenience method for calling [`set(_:forKey:)`](userdefaults/set(_:forkey:)-8ab6d.md).

## Parameters

- `value`: The integer value to store in the defaults database.
- `defaultName`: The key with which to associate the value.

## See Also

- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func set(Any?, forKey: String)](userdefaults/set(_:forkey:)-8ab6d.md)
  Sets the value of the specified default key.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified default key to the specified float value.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified default key to the double value.
- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified default key to the specified Boolean value.
- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified default key to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-3v852)*