# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets a data object for the specified key in the key-value store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func set(_ aData: Data?, forKey aKey: String)
```

#### Discussion

Using an [`NSData`](nsdata.md) object as a value in key-value storage lets you store arbitrary data. For example, in a game app, you can use it to store game state to iCloud.

Be sure to exercise caution when storing a data object. Because it is available to be read and modified by every instance of your app attached to a user’s iCloud account, some of which may be older versions or running on another platform, you must diligently protect a data object’s integrity. For more information, see “Exercise Caution When Using NSData Objects as Values” in [`iCloud Design Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012094).

## Parameters

- `aData`: The data object to store. The total size of this data object (including any object overhead) must not exceed 1 MB.
- `aKey`: The key under which to store the value. The length of this key must not exceed 64 bytes using UTF8 encoding.

## See Also

- [func set([Any]?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-40a8f.md)
  Sets an array object for the specified key in the key-value store.
- [func set(Bool, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-8o8mq.md)
  Sets a Boolean value for the specified key in the key-value store.
- [func set([String : Any]?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9vmlm.md)
  Sets a dictionary object for the specified key in the key-value store.
- [func set(Double, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-1xml0.md)
  Sets a double value for the specified key in the key-value store.
- [func set(Int64, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-7tt20.md)
  Sets a `long long` value for the specified key in the key-value store.
- [func set(Any?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9e3de.md)
  Sets an object for the specified key in the key-value store.
- [func set(String?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-2rlp.md)
  Sets a string object for the specified key in the key-value store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-3ga7z)*