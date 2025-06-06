# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets the value of the specified default key.

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

The `value` parameter can be only property list objects: [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169), [`NSString`](nsstring.md), [`NSNumber`](nsnumber.md), [`NSDate`](nsdate.md), [`NSArray`](nsarray.md), or [`NSDictionary`](nsdictionary.md). For [`NSArray`](nsarray.md) and [`NSDictionary`](nsdictionary.md) objects, their contents must be property list objects. For more information, see [`What is a Property List?`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/AboutPropertyLists/AboutPropertyLists.html#//apple_ref/doc/uid/10000048i-CH3-54303) in [`Property List Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

Setting a default has no effect on the value returned by the [`object(forKey:)`](userdefaults/object(forkey:).md) method if the same key exists in a domain that precedes the application domain in the search list.

## Parameters

- `value`: The object to store in the defaults database.
- `defaultName`: The key with which to associate the value.

## See Also

- [func removeObject(forKey: String)](userdefaults/removeobject(forkey:).md)
  Removes the value of the specified default key.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified default key to the specified float value.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified default key to the double value.
- [func set(Int, forKey: String)](userdefaults/set(_:forkey:)-3v852.md)
  Sets the value of the specified default key to the specified integer value.
- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified default key to the specified Boolean value.
- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified default key to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-8ab6d)*