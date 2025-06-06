# OBEXError

**Framework**: IOBluetooth  
**Kind**: typealias

Codes for OBEX errors. If the return value was not in the following range, then it is most likely resulting from kernel code/IOKit, and you should consult IOReturn.h for those codes.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias OBEXError = Int32
```

## Topics

### Constants
- [var kOBEXErrorRangeMin: OBEXErrorCodes](kobexerrorrangemin.md)
- [var kOBEXErrorRangeMax: OBEXErrorCodes](kobexerrorrangemax.md)

## See Also

- [typealias OBEXError](obexerror.md)
  Codes for OBEX errors. If the return value was not in the following range, then it is most likely resulting from kernel code/IOKit, and you should consult IOReturn.h for those codes.
- [struct OBEXConnectFlagValues](obexconnectflagvalues.md)
  Flags for Connect command.
- [struct OBEXHeaderIdentifiers](obexheaderidentifiers.md)
  Identifiers for OBEX Headers.
- [struct OBEXNonceFlagValues](obexnonceflagvalues.md)
  Flags for Nonce command during digest challenge.
- [struct OBEXOpCodeCommandValues](obexopcodecommandvalues.md)
  Operation OpCode values for commands.
- [struct OBEXOpCodeResponseValues](obexopcoderesponsevalues.md)
  Response opCode values.
- [struct OBEXOpCodeSessionValues](obexopcodesessionvalues.md)
  Operation OpCode values for sessions. From the OBEX 1.3 specification.
- [struct OBEXPutFlagValues](obexputflagvalues.md)
- [struct OBEXRealmValues](obexrealmvalues.md)
  Values for Realm during digest response.
- [struct OBEXSessionEventTypes](obexsessioneventtypes.md)
  Type identifiers for OBEX sessions.
- [struct OBEXSessionParameterTags](obexsessionparametertags.md)
  Tags for SessionParameters.
- [struct OBEXVersions](obexversions.md)
  The available/supported OBEX versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexerror)*