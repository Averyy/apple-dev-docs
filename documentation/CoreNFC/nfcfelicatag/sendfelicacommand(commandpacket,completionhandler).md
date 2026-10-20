# sendFeliCaCommand(commandPacket:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the FeliCa command packet data to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func sendFeliCaCommand(commandPacket: Data, completionHandler: @escaping @Sendable (Data, (any Error)?) -> Void)
```

```swift
func sendFeliCaCommand(commandPacket: Data) async throws -> Data
```

```objc
- (void) sendFeliCaCommandPacket:(NSData *) commandPacket completionHandler:(void (^)(NSData *responsePacket, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/sendfelicacommand(commandpacket:completionhandler:))*