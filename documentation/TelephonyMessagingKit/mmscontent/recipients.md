# recipients

**Framework**: TelephonyMessagingKit  
**Kind**: property

The recipients of the MMS message, as an array of MMS handles.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var recipients: [MMSHandle]
```

#### Discussion

When this array contains any elements, it may imply that the corresponding message is a group MMS. To determine if the message is a group MMS, inspect the value of the [`from`](mmscontent/from.md) property for multiple distinct handles. For example, if `recipients == [A]` and `from == B`, then the MMS uses a group consisting of `A`, `B`, and the person using the app.

## See Also

- [var from: MMSHandle?](mmscontent/from.md)
  The sender of the MMS message.
- [struct MMSHandle](mmshandle.md)
  A structure that represents an MMS address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent/recipients)*