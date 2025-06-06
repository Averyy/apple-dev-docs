# gss_iter_creds_f(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Iterates over all credentials with a user context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_iter_creds_f(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID?, _ userctx: UnsafeMutableRawPointer?, _ useriter: (UnsafeMutableRawPointer?, gss_OID?, gss_cred_id_t?) -> Void) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a description of other status outputs.

#### Discussion

Use the [`gss_iter_creds(_:_:_:_:)`](gss_iter_creds(_:_:_:_:).md) function if you don’t need the user context parameter.

## Parameters

- `flags`: No flags are currently defined. Pass 0 for this parameter.
- `mech`: The mechanism type of credentials to iterate over. Pass in   to iterate over all credentials.
- `userctx`: A user context that you use to keep track of callbacks.
- `useriter`: A block that is called once for each credential. The block receives the user context that you specified with the   parameter, the credential’s mechanism, and a copy of the credential as input on each iteration. Free the copy’s memory with a call to   when you are done with it. The block is called one final time with a   credential upon reaching the end of the list.

## See Also

- [func gss_iter_creds(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID?, (gss_OID?, gss_cred_id_t?) -> Void) -> OM_uint32](gss_iter_creds(_:_:_:_:).md)
  Iterates over all credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_iter_creds_f(_:_:_:_:_:))*