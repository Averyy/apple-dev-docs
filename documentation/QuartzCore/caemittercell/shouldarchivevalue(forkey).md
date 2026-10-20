# shouldArchiveValue(forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the value for a given key should be archived.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

```objc
- (BOOL) shouldArchiveValueForKey:(NSString *) key;
```

#### Return Value

[`true`](../../Swift/true.md) if the specified property should be archived, otherwise [`false`](../../Swift/false.md).

#### Discussion

The default implementation returns [`true`](../../Swift/true.md). This method is called by the object’s implementation of `encodeWithCoder:`.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

### Using Key-Value Coding Extensions
- [class func defaultValue(forKey: String) -> Any?](./defaultvalue%28forkey%29.md)
  Returns the default value of the property with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/shouldarchivevalue(forkey:))*