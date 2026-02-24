# setConnectionCodeSigningRequirement(_:)

**Framework**: Foundation  
**Kind**: method

Sets the code signing requirement for connections to this listener.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func setConnectionCodeSigningRequirement(_ requirement: String)
```

#### Discussion

Use this method to enforce a code-signing requirement on incoming XPC connections.

The following example shows how a listener can ensure that the XPC client service on the other end of a connection has a specific entitlement.

**Swift**:

```swift
func listener(_ listener: NSXPCListener,
                      shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool {
    newConnection.exportedObject = MyExportedObject()
    newConnection.exportedInterface = NSXPCInterface(with: MyExportedObjectProtocol.self)
    newConnection.setCodeSigningRequirement("entitlement [com.example.testentitlement] exists")
    newConnection.resume()
    return true
}
```

**Objective-C**:

```objc
- (BOOL)listener:(NSXPCListener *)listener shouldAcceptNewConnection:(NSXPCConnection *)newConnection {
    MyExportedObject *e = [[MyExportedObject new] autorelease];
    newConnection.exportedObject = e;
    newConnection.exportedInterface = [NSXPCInterface interfaceWithProtocol:@protocol(MyExportedObjectProtocol)];
    
    // This is an entitlement that must exist on the incoming connection's app signature
    [newConnection setCodeSigningRequirement:@"entitlement [com.example.testentitlement] exists"];
    [newConnection resume];

    return YES;
}
```

## Parameters

- `requirement`: A string that describes requirements expected of the connection peer. See [`Code Signing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/) for more information on the code signing format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/setconnectioncodesigningrequirement(_:))*