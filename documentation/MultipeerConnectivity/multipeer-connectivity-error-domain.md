# Multipeer Connectivity Error Domain

**Framework**: Multipeer Connectivity

The error domain for errors specific to Multipeer Connectivity.

## Topics

### Constants
- [let MCErrorDomain: String](mcerrordomain.md)
  The `NSError` domain constant. If the `domain` value for an `NSError` object is equal to `MCErrorDomain`, then the error was produced by the Multipeer Connectivity framework itself, as opposed to a lower-level framework on which it depends.

## See Also

- [enum MCSessionSendDataMode](mcsessionsenddatamode.md)
  Indicates whether delivery of data should be guaranteed.
- [enum MCSessionState](mcsessionstate.md)
  Indicates the current state of a given peer within a session.
- [enum MCEncryptionPreference](mcencryptionpreference.md)
  Indicates whether a session should use encryption when communicating with nearby peers.
- [MCError.Code](mcerror/code.md)
  Error codes found in [`MCErrorDomain`](mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.
- [Minimum and Maximum Supported Peers](minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/multipeer_connectivity_error_domain)*