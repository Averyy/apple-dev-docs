# MTRDeviceController

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRDeviceController
```

## Mentions

- [Onboarding a Matter device](onboarding-a-matter-device.md)

## Topics

### Initializers
- [init(parameters: MTRDeviceControllerAbstractParameters) throws](mtrdevicecontroller/init(parameters:).md)
### Instance Properties
- [var controllerNodeID: NSNumber?](mtrdevicecontroller/controllernodeid-6a04u.md)
- [var controllerNodeId: NSNumber?](mtrdevicecontroller/controllernodeid-6a03y.md)
- [var isRunning: Bool](mtrdevicecontroller/isrunning.md)
- [var uniqueIdentifier: UUID](mtrdevicecontroller/uniqueidentifier.md)
- [var devices: [MTRDevice]](mtrdevicecontroller/devices.md)
  Returns the list of MTRDevice instances that this controller has loaded into memory. Returns an empty array if no devices are in memory.
- [var isSuspended: Bool](mtrdevicecontroller/issuspended.md)
  If true, the controller has been suspended via `suspend` and not resumed yet.
- [var nodesWithStoredData: [NSNumber]](mtrdevicecontroller/nodeswithstoreddata.md)
  Returns the list of node IDs for which this controller has stored information.  Returns empty list if the controller does not have any information stored.
### Instance Methods
- [func add(MTRServerEndpoint) -> Bool](mtrdevicecontroller/add(_:).md)
- [func attestationChallenge(forDeviceID: NSNumber) -> Data?](mtrdevicecontroller/attestationchallenge(fordeviceid:).md)
- [func cancelCommissioning(forNodeID: NSNumber) throws](mtrdevicecontroller/cancelcommissioning(fornodeid:).md)
- [func commissionDevice(UInt64, commissioningParams: MTRCommissioningParameters) throws](mtrdevicecontroller/commissiondevice(_:commissioningparams:).md)
- [func commissionNode(withID: NSNumber, commissioningParams: MTRCommissioningParameters) throws](mtrdevicecontroller/commissionnode(withid:commissioningparams:).md)
- [func computePaseVerifier(UInt32, iterations: UInt32, salt: Data) -> Data?](mtrdevicecontroller/computepaseverifier(_:iterations:salt:).md)
- [func continueCommissioningDevice(UnsafeMutableRawPointer, ignoreAttestationFailure: Bool) throws](mtrdevicecontroller/continuecommissioningdevice(_:ignoreattestationfailure:).md)
- [func deviceBeingCommissioned(withNodeID: NSNumber) throws -> MTRBaseDevice](mtrdevicecontroller/devicebeingcommissioned(withnodeid:).md)
- [func fetchAttestationChallenge(forDeviceId: UInt64) -> Data?](mtrdevicecontroller/fetchattestationchallenge(fordeviceid:).md)
- [func getBaseDevice(UInt64, queue: dispatch_queue_t, completionHandler: MTRDeviceConnectionCallback) -> Bool](mtrdevicecontroller/getbasedevice(_:queue:completionhandler:).md)
- [func getDeviceBeingCommissioned(UInt64) throws -> MTRBaseDevice](mtrdevicecontroller/getdevicebeingcommissioned(_:).md)
- [func openPairingWindow(UInt64, duration: Int) throws](mtrdevicecontroller/openpairingwindow(_:duration:).md)
- [func openPairingWindow(withPIN: UInt64, duration: Int, discriminator: Int, setupPIN: Int) throws -> String](mtrdevicecontroller/openpairingwindow(withpin:duration:discriminator:setuppin:).md)
- [func pairDevice(UInt64, address: String, port: UInt16, setupPINCode: UInt32) throws](mtrdevicecontroller/pairdevice(_:address:port:setuppincode:).md)
- [func pairDevice(UInt64, discriminator: UInt16, setupPINCode: UInt32) throws](mtrdevicecontroller/pairdevice(_:discriminator:setuppincode:).md)
- [func pairDevice(UInt64, onboardingPayload: String) throws](mtrdevicecontroller/pairdevice(_:onboardingpayload:).md)
- [func preWarmCommissioningSession()](mtrdevicecontroller/prewarmcommissioningsession.md)
- [func remove(MTRServerEndpoint, queue: dispatch_queue_t, completion: () -> Void)](mtrdevicecontroller/remove(_:queue:completion:).md)
- [func setDeviceControllerDelegate(any MTRDeviceControllerDelegate, queue: dispatch_queue_t)](mtrdevicecontroller/setdevicecontrollerdelegate(_:queue:).md)
- [func setNocChainIssuer(any MTRNOCChainIssuer, queue: dispatch_queue_t)](mtrdevicecontroller/setnocchainissuer(_:queue:).md)
- [func setPairingDelegate(any MTRDevicePairingDelegate, queue: dispatch_queue_t)](mtrdevicecontroller/setpairingdelegate(_:queue:).md)
- [func setupCommissioningSession(with: MTRSetupPayload, newNodeID: NSNumber) throws](mtrdevicecontroller/setupcommissioningsession(with:newnodeid:).md)
- [func setupCommissioningSession(withDiscoveredDevice: MTRCommissionableBrowserResult, payload: MTRSetupPayload, newNodeID: NSNumber) throws](mtrdevicecontroller/setupcommissioningsession(withdiscovereddevice:payload:newnodeid:).md)
- [func shutdown()](mtrdevicecontroller/shutdown.md)
- [func startBrowse(forCommissionables: any MTRCommissionableBrowserDelegate, queue: dispatch_queue_t) -> Bool](mtrdevicecontroller/startbrowse(forcommissionables:queue:).md)
- [func stopBrowseForCommissionables() -> Bool](mtrdevicecontroller/stopbrowseforcommissionables.md)
- [func stopDevicePairing(UInt64) throws](mtrdevicecontroller/stopdevicepairing(_:).md)
- [func add(any MTRDeviceControllerDelegate, queue: dispatch_queue_t)](mtrdevicecontroller/add(_:queue:).md)
  Adds a Delegate to the device controller as well as the Queue on which the Delegate callbacks will be triggered
- [func forgetDevice(withNodeID: NSNumber)](mtrdevicecontroller/forgetdevice(withnodeid:).md)
  Forget any information we have about the device with the given node ID.  That includes clearing any information we have stored about it.
- [func remove(MTRServerEndpoint)](mtrdevicecontroller/remove(_:)-2i5l5.md)
  Remove the given server endpoint without being notified when the removal completes.
- [func remove(any MTRDeviceControllerDelegate)](mtrdevicecontroller/remove(_:)-8pxve.md)
  Removes a Delegate from the device controller
- [func resume()](mtrdevicecontroller/resume.md)
  Resume the controller.  This has no effect if the controller is not suspended.
- [func suspend()](mtrdevicecontroller/suspend.md)
  Suspend the controller.  This will attempt to stop all network traffic associated with the controller.  The controller will remain suspended until it is resumed.
### Type Methods
- [class func computePASEVerifier(forSetupPasscode: NSNumber, iterations: NSNumber, salt: Data) throws -> Data](mtrdevicecontroller/computepaseverifier(forsetuppasscode:iterations:salt:).md)
- [class func decodeXPCReadParams([String : Any]?) -> MTRReadParams?](mtrdevicecontroller/decodexpcreadparams(_:).md)
- [class func decodeXPCResponseValues([[String : Any]]?) -> [[String : Any]]?](mtrdevicecontroller/decodexpcresponsevalues(_:).md)
- [class func decodeXPCSubscribeParams([String : Any]?) -> MTRSubscribeParams?](mtrdevicecontroller/decodexpcsubscribeparams(_:).md)
- [class func encodeXPCReadParams(MTRReadParams) -> [String : Any]?](mtrdevicecontroller/encodexpcreadparams(_:).md)
- [class func encodeXPCResponseValues([[String : Any]]?) -> [[String : Any]]?](mtrdevicecontroller/encodexpcresponsevalues(_:).md)
- [class func encodeXPCSubscribeParams(MTRSubscribeParams?) -> [String : Any]?](mtrdevicecontroller/encodexpcsubscribeparams(_:).md)
- [class func sharedController(withID: (any NSCopying)?, xpcConnect: MTRXPCConnectBlock) -> MTRDeviceController](mtrdevicecontroller/sharedcontroller(withid:xpcconnect:)-5yhq4.md)
- [class func sharedController(withId: (any NSCopying)?, xpcConnect: MTRXPCConnectBlock) -> MTRDeviceController](mtrdevicecontroller/sharedcontroller(withid:xpcconnect:)-6rg64.md)
- [class func xpcInterfaceForClientProtocol() -> NSXPCInterface](mtrdevicecontroller/xpcinterfaceforclientprotocol.md)
- [class func xpcInterfaceForServerProtocol() -> NSXPCInterface](mtrdevicecontroller/xpcinterfaceforserverprotocol.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller)*