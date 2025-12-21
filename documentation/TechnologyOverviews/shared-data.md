# Shared data

**Framework**: Technology Overviews

Share data with your apps running on different devices using iCloud, or share data between your app and app extensions.

Share data to help people access what they need wherever they are, and to make sure your own apps are able to coordinate. If you build multiple apps, build an app for multiple devices, or deliver app extensions inside your apps, consider how you might share data between different processes.

#### Make Your Apps Content Available on Multiple Devices

When developing apps, choose the iCloud technology that works best for the data you want to share. You can share a small amount of data, or a lot. You can even adopt multiple iCloud technologies in the same app.

-  Developers of multiplatform games adopt the [`GameSave`](https://developer.apple.com/documentation/GameSave) framework to synchronize game data among someone’s devices using iCloud. The framework handles common syncing scenarios like conflict resolution and offline play.
-  Store discrete values related to app preferences, app configuration, or app state using iCloud key-value storage. The [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/Foundation/NSUbiquitousKeyValueStore) type is similar to the defaults database you use to manage preferences. Use it to store scalar values and property-list object types, including numbers, strings, dates, and small amounts of data, arrays, and dictionaries. You can store a maximum of 1024 keys and 1 megabyte of data.
-  Store someone’s personal documents in iCloud Drive using iCloud document storage. With this feature, your app gains access to an app-specific directory in the person’s iCloud storage. Fetch this directory using the [`url(forUbiquityContainerIdentifier:)`](https://developer.apple.com/documentation/Foundation/FileManager/url(forUbiquityContainerIdentifier:)) method, and make it the default location for storing a person’s files.
-  Adopt [`Syncing model data across a person’s devices`](https://developer.apple.com/documentation/SwiftData/Syncing-model-data-across-a-persons-devices) or [`Mirroring a Core Data store with CloudKit`](https://developer.apple.com/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit), which work with [`CloudKit`](https://developer.apple.com/documentation/CloudKit) to store your app’s data. You can also adopt [`CloudKit`](https://developer.apple.com/documentation/CloudKit) directly, or use [`CloudKit JS`](https://developer.apple.com/documentation/CloudKitJS) to add CloudKit support to your web app. Get up to 1PB of storage for your app’s public data, and create containers for people to share content with each other. Run integration tests of your CloudKit code from Xcode or your continuous integration system. Access performance metrics, telemetry data, logs, and more using tools like [`CloudKit Console`](https://developer.apple.comhttps://icloud.developer.apple.com/dashboard/).

[`Configuring iCloud services`](https://developer.apple.com/documentation/Xcode/configuring-icloud-services) your app uses in Xcode. Each service requires specific entitlements to validate your app’s access to a person’s iCloud storage.

> **Note**: Devices that access iCloud must have a network connection and a valid Apple Account. Devices can operate without network access for a period of time after the initial login, relying on previously downloaded data.

#### Share Content on the Same Device

To protect apps from nefarious code, Apple places them in  on nearly all devices. Each sandbox includes a container directory, which only the owning app can access. To share files between two apps you create, or between your app and an app extension, configure an [`Configuring app groups`](https://developer.apple.com/documentation/Xcode/configuring-app-groups) for both processes. A process with the [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups) can [`containerURL(forSecurityApplicationGroupIdentifier:)`](https://developer.apple.com/documentation/Foundation/FileManager/containerURL(forSecurityApplicationGroupIdentifier:)) of the app group directory, and access files in that directory.

![An illustration of an app and app extension sharing data using an app group.](https://docs-assets.developer.apple.com/published/4f5d1e8fc8235baaff997d1e967ac76c/data-management-share-content-between-different-processes.png)

The creation of an app group creates a shared space on disk for multiple processes to share files. It also enables additional interprocess communication (IPC) between those processes using Mach IPC, POSIX semaphores and shared memory, UNIX domain sockets, and other IPC mechanisms. In macOS, app groups facilitate communication between sandboxed apps, and between sandboxed and nonsandboxed apps. Apps can belong to one or more app groups.

#### Deploy Your Own Shared Remote File Server

If you manage your own server-side storage, create a File Provider extension to access that remote storage. A File Provider extension monitors and manages the local copy of documents someone places on your remote server. When someone changes a local file, the extension uploads the modified file to your server. Similarly, when the file changes on the server, the extension downloads the file and updates the local storage.

Create your extension using the [`File Provider`](https://developer.apple.com/documentation/FileProvider) and [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) frameworks. Deploy your app extension inside an app you offer to your customers to manage their access to your system.

#### Coordinate Access to Shared Files

File coordination is essential if you read and write files in iCloud, in an app group, or in any shared space. File coordinators prevent multiple processes from accessing a file in a conflicting way. For example, file coordinators prevent two processes from writing to the same file simultaneously. You adopt file coordinators in one of the following ways:

#### Design Custom Document Formats for Sharing

If your app uses a custom file format for documents, [`iCloud`](https://developer.apple.com/design/Human-Interface-Guidelines/icloud) to operate well on all platforms. iCloud document storage lets someone open files on iPhone, iPad, Mac, and other devices.

-  If your document contains several different types of data, consider using a file package to store each type of data separately. A file package is a directory that the system presents as a single file in appropriate situations. When you modify files in the package, the system transfers only the files that changed to iCloud.
-  Differences between platforms might require you to pick a format for your data and use it on all platforms. For example, the positive y-axis points in different directions in iOS and macOS, requiring you to convert coordinate values on one of the platforms.
-  Version numbers are always a good idea, especially when accessing your documents on different device types. Handle documents with older version numbers gracefully, and alert someone if they try to open a document with an unsupported version number.
-  In addition to document-specific data, include app-specific state that applies to your documents in your custom file formats. For example, a drawing app might store the currently selected tool and drawing colors with the rest of the document data. Don’t store transient state that might impact the experience with your app from one device to another. For example, don’t store the current scroll position of the document window. Use a file package to store any app-related state separately from your document data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/shared-data)*