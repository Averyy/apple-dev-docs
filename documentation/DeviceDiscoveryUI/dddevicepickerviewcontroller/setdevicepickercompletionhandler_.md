# setDevicePickerCompletionHandler:

**Framework**: DeviceDiscoveryUI  
**Kind**: method  
**Role**: Instance Method

Sets the completion handler that the system calls when the user selects a device from the picker view.

**Availability**:
- tvOS 16.0+

## Declaration

```objc
- (void) setDevicePickerCompletionHandler:(void (^)(nw_endpoint_t endpoint, nw_error_t error)) devicePickerCompletionHandler;
```

## Mentions

- [Connecting a tvOS app to other devices over the local network](../connecting-a-tvos-app-to-other-devices-over-the-local-network.md)

## Discussion

The system calls this block after the user selects a device from the endpoint picker view. If the user cancels the view, the picker silently closes.

```swift
// This example uses the default application services parameters;
// however, you can add a NWProtocolFramer to provide application-level
// messaging.
nw_browse_descriptor_t browseDescriptor = nw_browse_descriptor_create_application_service("MyAppService");

nw_parameters_t parameters = nw_parameters_create();

// Create the view controller for the endpoint picker.
NWEndpointPickerViewController *endpointPickerViewController = [[NWEndpointPickerViewController alloc] initWithBrowseDescriptor:browseDescriptor parameters: parameters];

// Set the endpoint picker handler.
[endpointPickerViewController setEndpointPickerCompletionHandler:^(nw_endpoint_t  _Nullable endpoint, nw_error_t  _Nullable error) {
    // Connect to the endpoint here.
    [self.myConnectionController connectToEndpoint: endpoint];
}];

 // Show the network device picker as a full-screen, modal view.
[self presentViewController:endpointPickerViewController animated:YES completion:nil];
```

## Parameters

- `devicePickerCompletionHandler`: A block that the system calls after the user selects a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller/setdevicepickercompletionhandler:)*