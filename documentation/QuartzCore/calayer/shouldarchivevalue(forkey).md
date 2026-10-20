# shouldArchiveValue(forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean indicating whether the value of the specified key should be archived.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
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

[`true`](../../Swift/true.md) if the specified property should be archived or [`false`](../../Swift/false.md) if it should not.

#### Discussion

The default implementation returns [`true`](../../Swift/true.md).

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

### Key-value coding extensions
- [class func defaultValue(forKey: String) -> Any?](./defaultvalue%28forkey%29.md)
  Specifies the default value associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/shouldarchivevalue(forkey:))*