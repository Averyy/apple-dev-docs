# Configuring your app for ultra-constrained networks

**Framework**: Bundle Resources

Prepare to deliver data over resource-limited data networks.

#### Overview

Carrier-provided satellite networks are called . An ultra-constrained network has limited throughput, high latency, limited capacity, and intermittent loss of connectivity, all of which directly affect the performance of the apps that run on the network.

With limited bandwidth and availability, ultra-constrained networks aren’t a good choice for a number of data types and activities that are possible on unconstrained networks. Some general best practices to follow while using ultra-constrained networks include:

- Block or delay noncritical uploads and downloads.
- Use small, infrequent messages.
- Avoid frequent polling by using retry with  — a process by which you decrease the rate your app attempts to send data over the network in order to conserve network bandwidth.
- Cache data and batch requests.
- Avoid accessing streaming media.
- Minimize large background downloads and uploads.
- Minimize and optimize the use of real-time data, for instance by creating app-level resilience to breaks in service or availability.

#### Configure Your App to Access Ultra Constrained Networks

iOS enables apps to send data over ultra-constrained networks — or “opt-in by default” — but also makes it possible for carriers to dedicate traffic for specific use cases over the satellite networks they provide and limit data usage.

To ensure your app can use ultra-constrained networks on all providers, add the [`com.apple.developer.networking.carrier-constrained.appcategory`](Entitlements/com.apple.developer.networking.carrier-constrained.appcategory.md) entitlement to your app and provide an array of strings that define the service categories your app provides. The entitlement’s documentation provides specific values for a variety of app categories.

> **Note**: To opt out of using ultra-constrained networks, set the [`allowUltraConstrainedPaths`](https://developer.apple.com/documentation/Network/NWParameters/allowUltraConstrainedPaths) property to `false`.

#### Implement a Network Path Monitor to Limit Use of Resources

To ensure your app operates within the limits of ultra-constrained networks, implement a network path monitor to ensure that the data your app sends uses network resources appropriately. If you determine your app is on an ultra-constrained network, you can disable high-bandwidth features, as shown in this example.

```swift
import Network

let monitor = NWPathMonitor()
let queue = DispatchQueue(label: "CarrierUltraConstrainedMonitor")

monitor.pathUpdateHandler = { path in
    if path.isUltraConstrained {
        print("Network is ultra-constrained.")
        // Apply ultra-constrained optimizations here, for example:
        //   - Disable image or video uploads.
        //   - Send messages as compressed plaintext.
        //   - Retry failed messages after a back-off period.
    } else {
        print("Network is not ultra-constrained.")
        // Resume normal behavior.
    }
}

monitor.start(queue: queue)
```

The monitor runs in the background, and the system calls the handler you provide to inform the app when the network path type changes. This process allows an app to enable, disable, and then re-enable higher bandwidth features as necessary.

#### Test Your App and Certify Optimization

After you implement a network path monitor, test your app in a variety of conditions to ensure that it uses ultra-constrained network resources appropriately. Once you’ve optimized your app, add the [`com.apple.developer.networking.carrier-constrained.app-optimized`](Entitlements/com.apple.developer.networking.carrier-constrained.app-optimized.md) entitlement to certify the network optimization of your app. This entitlement ensures a seamless experience for people using your app, removing system alerts that ask for permission to use the network.

## See Also

- [Information Property List](Information-Property-List.md)
  A resource containing key-value pairs that identify and configure a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/configuring-your-app-for-ultra-constrained-networks)*