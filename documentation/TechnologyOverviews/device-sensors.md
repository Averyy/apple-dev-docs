# Device sensors

**Framework**: Technology Overviews

Adjust your app’s behavior using contextual data you receive from a device’s built-in sensors.

Hardware sensors provide your app with information about the world or details about the device’s physical state. Sensors include accelerometers, gyroscopes, magnetometers, LiDAR, cameras, GPS, NFC, barometers, and more. Use the data from these sensors as direct input to your app, or as additional context to improve the experience of using your app. For example:

- Filter data based on someone’s geographic location.
- Use device-related motion as direct input to a game.
- Detect objects in a person’s surrounding environment and annotate them with information.
- Apply course, heading, location, and altitude information to hiking or driving directions.
- Find other nearby devices and exchange data with them securely.

#### Obtain Access to the Relevant Hardware

System frameworks limit access to some types of sensor data, making that data available only to apps that receive proper authorization. Request that authorization programmatically using the APIs that your framework provides. In addition to that request, provide a localized description of how you intend to use the data in your app’s [`Managing your app’s information property list values`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list#Configure-information-property-list-values). When presenting your request, the system displays your description to help the person make an informed choice about whether to grant access.

The following table lists sensors you might find on an Apple device, along with the frameworks that provide access. The table also lists any usage description keys to include in your app’s
[`Managing your app’s information property list values`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list#Configure-information-property-list-values).

| Hardware type | Framework | Usage description keys |
| --- | --- | --- |
| Accelerometer and gyroscope data (device motion) | [`Core Motion`](https://developer.apple.com/documentation/CoreMotion) | Not required |
| Bluetooth (communication) | [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth) | [`NSBluetoothAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription) |
| Camera (image capture) | [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation#Capture) | [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) |
|  |  | [`NSMainCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMainCameraUsageDescription) |
| Camera and LiDAR (environment capture) | [`ARKit`](https://developer.apple.com/documentation/ARKit) | [`NSWorldSensingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSWorldSensingUsageDescription) |
|  |  | [`NSHandsTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHandsTrackingUsageDescription) |
|  |  | [`NSAccessoryTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessoryTrackingUsageDescription) |
| Location data (global positioning) | [`Core Location`](https://developer.apple.com/documentation/CoreLocation) | [`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription) |
|  |  | [`NSLocationAlwaysAndWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription) |
| Microphone (audio input) | [`AVFAudio`](https://developer.apple.com/documentation/AVFAudio) | [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) |
| Near field communication (NFC) | [`Core NFC`](https://developer.apple.com/documentation/CoreNFC) | [`NFCReaderUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NFCReaderUsageDescription) |
| Pedometer, motion recording, and fall detection (health data) | [`Core Motion`](https://developer.apple.com/documentation/CoreMotion) | [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) |
|  |  | [`NSFallDetectionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription) |
| General sensor data (research) | [`SensorKit`](https://developer.apple.com/documentation/SensorKit) | [`NSSensorKitUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDescription) |

> **Note**: If your app generates personal information from sensor data, it’s important to secure that data. Individual samples from a sensor might not represent personally sensitive information, but a larger set of samples might. For example, the [`Core Motion`](https://developer.apple.com/documentation/CoreMotion#Pedometer-and-fitness) uses accumulated accelerometer and gyroscope data to determine step counts and fitness information, which is personal health data.

#### Minimize the Amount of Sensor Data You Collect

Enable sensors only when you need the data they offer, and disable them again as soon as you have what you need. For example, start collecting pedometer data when someone starts a workout, and stop collecting that data when the workout ends. Enabling a sensor at the last second prevents it from generating data your app won’t use. Disabling the sensor when you’re done prevents unnecessary collection, and also gives the system the option to power down the associated hardware to save energy.

In the framework for a given sensor, look for APIs that reduce the amount of time spent collecting data when properly configured. Some sensors offer variable data collection rates, or configurable accuracy. For example, location services let you specify the level of precision you require for location values. If you’re using someone’s location to search for nearby restaurants, an approximate location helps your app narrow the list of results. Reducing the accuracy or frequency of updates helps the system manage your app’s power usage, and improve battery life.

#### Apply Someones Location to Your Apps Content

Incorporate location data into your app to improve the experience people have using your app. Location data provides context for interpreting or displaying your app’s content. A to-do app might remind someone to pick up their clothes when they’re close to the dry cleaner. Apps that search for real-world points of interest can limit results to those that are nearby. An app that provides driving or walking directions can use the person’s location to guide them to their destination.

The system handles the collection of the data needed to triangulate someone’s location. After computing a location, the system delivers it asynchronously to apps that requested the information. Calculating someone’s position might entail the use of cellular, Wi-Fi, or GPS radios for an extended period of time.

To help you manage your app’s power usage, the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) framework offers different [`Getting the current location of a device`](https://developer.apple.com/documentation/CoreLocation/getting-the-current-location-of-a-device) with different power requirements. Choose the service that best suits your needs, and combine services in creative ways to reduce your app’s power usage further. For example, you might use a low-power service to determine when someone is in a specific geographic region, and then enable the higher-powered [`startUpdatingLocation()`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/startUpdatingLocation()) to collect precise location values while they’re in that region.

Make every effort to turn off location services when you don’t need them. Apart from navigation apps, most apps don’t need constant location updates. Apps with legitimate reasons can request [`Handling location updates in the background`](https://developer.apple.com/documentation/CoreLocation/handling-location-updates-in-the-background) as needed, but try to find alternatives to collecting locations. For example, apps that implement location sharing among friends can use a [`Core Location`](https://developer.apple.com/documentation/CoreLocation#Location-push-service-extension) to deliver those updates in a way that uses power thoughtfully.

The system provides each location value as a geographical latitude and longitude. To convert these coordinates to a more people-friendly address, create a [`MKReverseGeocodingRequest`](https://developer.apple.com/documentation/MapKit/MKReverseGeocodingRequest). The [`GeoToolbox`](https://developer.apple.com/documentation/GeoToolbox) also provides utilities to working with addresses and place-names.

#### Track Device Related Motion

Many Apple devices have sensors that report device-related movements, the device’s attitude in space, its altitude relative to sea level, and other motion-related details. You can use this data as contextual information, or as a form of input to your app. For example, a game might use accelerometer and gyroscope values as input.

To retrieve live motion-related data, adopt the [`Core Motion`](https://developer.apple.com/documentation/CoreMotion) framework. This framework delivers raw data for the onboard accelerometers, gyroscopes, magnetometer, and barometer on portable devices such as iPhone, iPad, Apple Watch, [`visionOS`](https://developer.apple.com/documentation/visionos), and even some [`CMHeadphoneMotionManager`](https://developer.apple.com/documentation/CoreMotion/CMHeadphoneMotionManager). The framework also offers processed versions of many types of data, which give you ready-to-use information such as course and heading values, pedometer data, and the device’s attitude vector relative to the ground.

When you want to analyze sensor data over a longer period of time, use [`SensorKit`](https://developer.apple.com/documentation/SensorKit). This framework records sensor data for a period of time you designate and delivers the resulting samples for analysis. SensorKit supports most of the same sensors as Core Motion, and many other types of sensors. For example, use it to analyze ambient light values, wrist temperature, heart rate, and device-usage metrics.

Even if you don’t collect sensor data for your app, the system still uses sensor data for specific features. On iPhone and iPad, the system uses the accelerometers to determine the device’s orientation relative to the ground and detect changes between portrait and landscape orientations. System apps like Workout and Fitness use sensor data to record workouts and contribute that information to a person’s health data.

#### Capture Information About Someones Surroundings

On iPhone and iPad, cameras can capture details about a person’s surroundings and make it available to your app. On [`visionOS`](https://developer.apple.com/documentation/visionos), the camera input is an integral part of a person’s experience, and the system blends that input with your app’s content seamlessly. System frameworks also have access to the camera input, and you use these frameworks to:

- Implement an augmented reality app.
- Identify people, pets, images, bar codes, text, and other objects.
- Measure distances between objects.

If you’re creating an augmented reality app for iPhone or iPad, use [`ARKit`](https://developer.apple.com/documentation/ARKit) to manage the live camera content. This framework analyzes the environment and provides anchor points for attaching custom content. For example, anchor an image to a wall to create the appearance of a poster on that wall. As the person moves their device, ARKit updates the position of your custom content to maintain the illusion that it’s part of the person’s environment.

To capture details about a person’s environment on iPhone or iPad, adopt the [`VisionKit`](https://developer.apple.com/documentation/VisionKit) or [`Vision`](https://developer.apple.com/documentation/Vision) framework. These frameworks use machine learning to analyze and classify content in images or video you provide. VisionKit detects text, URLs, QR codes, and some real-world objects, providing your app with a usable version of that content. For example, the framework can deliver the text from an image as a string to your app. Use the Vision framework to detect face and body poses, calculate an aesthetics score for an image, and perform other types of analysis or classification.

While ARKit manages interactions between virtual and real content in an augmented reality app, the [`RoomPlan`](https://developer.apple.com/documentation/RoomPlan) framework helps someone create a 3D model of their room, which you can then use in your app. The framework is meant for apps that help people plan out content in their environment. For example, an interior design app might use this framework to create a virtual version of someone’s room and place furniture and decorations. The framework requires you to present a [`RoomCaptureView`](https://developer.apple.com/documentation/RoomPlan/RoomCaptureView), which instructs the person how to scan their room, so you can’t capture environmental details casually.

#### Detect Nearby Devices and Ibeacons

Some apps use proximity to other devices to perform actions. For example, near-field communication (NFC) hardware allows someone to pay for things using their iPhone. Some government and commercial entities are also adopting NFC for identity verification. Many Apple devices also support iBeacon, which allows proximity detection in other situations.

If your app processes financial transactions, adopt Tap to Pay on iPhone as one of the payment methods. The [`ProximityReader`](https://developer.apple.com/documentation/ProximityReader) framework provides the payment UI for this feature, and works with your app to deliver the information your payment processor needs. The framework can also read and issue loyalty cards or verify someone’s identity against government-issued credentials someone adds to the Wallet app. To read custom tags or other information directly from the NFC hardware, use the [`Core NFC`](https://developer.apple.com/documentation/CoreNFC) framework.

To deliver information at a greater distance than NFC allows, use iBeacons and the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) framework. An iBeacon is a dedicated hardware device that you place in a location such as a museum or store. When someone using your app comes into the vicinity of the beacon, your app [`Determining the proximity to an iBeacon device`](https://developer.apple.com/documentation/CoreLocation/determining-the-proximity-to-an-ibeacon-device). For example, an iBeacon in a museum might cause your app to display information about the nearby exhibit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/device-sensors)*