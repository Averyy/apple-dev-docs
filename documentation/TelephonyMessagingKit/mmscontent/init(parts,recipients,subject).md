# init(parts:recipients:subject:)

**Framework**: TelephonyMessagingKit  
**Kind**: init  
**Role**: Initializer

Creates an MMS content instance with the provided values.

**Availability**:
- iOS 26.0+

## Declaration

```swift
init(parts: [MMSPartContent], recipients: [MMSHandle], subject: String? = nil)
```

## Parameters

- `parts`: The parts of the MMS.
- `recipients`: An array of handles representing the recipients of the message.
- `subject`: The subject of the MMS. Omit this parameter to leave the subject empty.

## See Also

### Creating an MMS content instance
- [init()](./init%28%29.md)
  Creates an empty MMS content instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent/init(parts:recipients:subject:))*