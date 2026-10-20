# matchesRecord(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Tests whether or not a record matches a search element.

**Availability**:
- macOS

## Declaration

```swift
func matchesRecord(_ record: ABRecord!) -> Bool
```

```objc
- (BOOL) matchesRecord:(ABRecord *) record;
```

#### Return Value

[`true`](../../Swift/true.md) if the `record` argument satisfies the conditions in the search element; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If `record` is `nil`, this method raises an exception.

## Parameters

- `record`: The record to be tested against the search object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchelement/matchesrecord(_:))*