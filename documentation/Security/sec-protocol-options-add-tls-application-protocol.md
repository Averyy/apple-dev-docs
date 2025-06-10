# sec_protocol_options_add_tls_application_protocol(_:_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func sec_protocol_options_add_tls_application_protocol(_ options: sec_protocol_options_t, _ application_protocol: UnsafePointer<CChar>)
```

#### Discussion

```None
 Add an application protocol supported by clients of this protocol instance.
```

## Parameters

- `options`: A   instance.
- `application_protocol`: A NULL-terminated string defining the application protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_add_tls_application_protocol(_:_:))*