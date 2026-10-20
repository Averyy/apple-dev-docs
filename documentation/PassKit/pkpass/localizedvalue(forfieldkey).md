# localizedValue(forFieldKey:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns the localized value for a specified field of the pass.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
func localizedValue(forFieldKey key: String) -> Any?
```

```objc
- (id) localizedValueForFieldKey:(NSString *) key;
```

#### Return Value

The localized value for the pass’s field.

#### Discussion

If your app works with passes from arbitrary sources, such as an email client, it can’t use this method because PassKit doesn’t know the keys for those passes in advance. Use the other properties of this class, such as [`organizationName`](./organizationname.md), instead.

## Parameters

- `key`: The field’s key as specified in the pass.

## See Also

### Getting the display attributes
- [var icon: UIImage](./icon.md)
  The pass icon.
- [var organizationName: String](./organizationname.md)
  The name of the organization that creates the pass.
- [var relevantDate: Date?](./relevantdate.md)
  The date when the pass is most likely to be useful or necessary.
- [class PKPassRelevantDate](../pkpassrelevantdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/localizedvalue(forfieldkey:))*