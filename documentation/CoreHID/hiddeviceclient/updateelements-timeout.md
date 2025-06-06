# updateElements(_:timeout:)

**Framework**: Core HID  
**Kind**: method

Provide new update values for, or request current values from, lists of elements.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func updateElements(_ updates: [any HIDElementUpdate], timeout: Duration? = nil) async -> HIDDeviceClient.HIDElementUpdateResult
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Return Value

A [`HIDDeviceClient.HIDElementUpdateResult`](hiddeviceclient/hidelementupdateresult.md) containing the result of each operation. Even if the overall call succeeds, individual updates may have failed.

#### Discussion

Multiple [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md) or [`HIDDeviceClient.RequestElementUpdate`](hiddeviceclient/requestelementupdate.md) objects can be passed in a list to stage a series of transactions to the device. The multi-update behavior can be helpful in providing updates to the device and immediately querying how it responded. All of the updates fail if another client obtains the device.

Example usage:

```swift
let elements = await client.elements
guard let capsLockKey = elements.filter({ $0.usage == .keyboardOrKeypad(usage: .keyboardCapsLock) }).first else {
    throw HIDDeviceError.unsupported
}
let provide = HIDDeviceClient.ProvideElementUpdate(values: [HIDElement.Value(element: capsLockKey, fromLogicalValueTruncatingIfNeeded: 1, timestamp: SuspendingClock.now)!])
let leds = elements.filter { $0.usage.page == HIDUsage.ledPage }
let request = HIDDeviceClient.RequestElementUpdate(elements: leds)
let results = await client.updateElements([provide, request])

try results[provide]?.get()
let resultVals = try results[request]?.get()
for value in resultVals! {
    continue
}
```

## Parameters

- `updates`: A list of updates to perform sequentially in the order that they are specified.
- `timeout`: The maximum amount of time to wait for the device to respond before the call times out and fails. Not providing a duration causes the client to wait forever. The timeout value is per update. If a number of milliseconds is specified, it waits up to that number of millseconds for each update. If one update times out, the remaining updates are aborted.

## See Also

- [HIDDeviceClient.RequestElementUpdate](hiddeviceclient/requestelementupdate.md)
  A request to pull the current value from a list of HID elements
- [HIDDeviceClient.ProvideElementUpdate](hiddeviceclient/provideelementupdate.md)
  A structure that provides values for a list of HID elements.
- [HIDDeviceClient.HIDElementUpdateResult](hiddeviceclient/hidelementupdateresult.md)
  A class to hold the results of an element update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/updateelements(_:timeout:))*