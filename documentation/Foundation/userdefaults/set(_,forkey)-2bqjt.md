# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the value of the specified key to a URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func set(_ url: URL?, forKey defaultName: String)
```

```objc
- (void) setURL:(NSURL *) url forKey:(NSString *) defaultName;
```

#### Discussion

This method handles file URLs differently than other types of URLs. For most URLs, the method stores the URL object as the root object of a [`Data`](../data.md) archive. If `url` contains a path to a file in the home directory, this method replaces the home directory portion of the path with a tilde (~) character before generating the data object. When you read the value back, the system expands the tilde character to the current home directory path.

If the location of a file might change, don’t use a file URL to specify its location. Instead, create a bookmark URL using the [`bookmarkData(withContentsOf:)`](../nsurl/bookmarkdata%28withcontentsof%29.md) method and save that URL instead. Bookmark URLs store additional information about the file so the system can locate the file later, even if the path to that file changes.

After you call this method, the system generates a [`didChangeNotification`](./didchangenotification.md) for registered observers.

## Parameters

- `url`: The value to store in the defaults database.
- `defaultName`: The key that contains the setting’s name.

## See Also

### Setting the value for a key
- [func set(Bool, forKey: String)](./set%28_,forkey%29-3nn5m.md)
  Sets the value of the specified key to a Boolean value.
- [func set(Int, forKey: String)](./set%28_,forkey%29-3v852.md)
  Sets the value of the specified key to an integer.
- [func set(Float, forKey: String)](./set%28_,forkey%29-1t5ec.md)
  Sets the value of the specified key to a floating-point number.
- [func set(Double, forKey: String)](./set%28_,forkey%29-2w22f.md)
  Sets the value of the specified key to a double.
- [func set(Any?, forKey: String)](./set%28_,forkey%29-8ab6d.md)
  Sets the value of the specified key to a property list object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/set(_:forkey:)-2bqjt)*