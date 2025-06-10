# Data management

**Framework**: Technology Overviews

Build your app’s data model, persist that data to disk or iCloud, and access people’s personal data.

Your app’s data drives everything you do, and Apple frameworks provide the types you need to represent that data. Build your data structures with basic types like numbers, strings, dates, URLs. Add collections and other types to organize large amounts of data. Persist data to disk securely, storing your app’s data in designated locations in the file system or in iCloud. Make use of someone’s music, contacts, photos, and other personal data in a privacy friendly way.

#### Standard Data Types and Processes

All apps use integers, floating-point numbers, strings, URLs, collections, and other primitive types to store data. When you use [`Swift Standard Library`](https://developer.apple.com/documentation/Swift/swift-standard-library) and the [`Foundation`](https://developer.apple.com/documentation/Foundation) framework, you get object-oriented versions of these types that work on all Apple platforms. These types also support security and convenience features that make them easier to use in your code.

#### Structured Data Models

Build a scalable and efficient data model for your app using technologies like [`SwiftData`](https://developer.apple.com/documentation/SwiftData) and [`Core Data`](https://developer.apple.com/documentation/CoreData). Both technologies offer straightforward ways to build your data structures, and fetch only the data you need. They also offer the features you’d expect, like persistence, undo support, and iCloud integration.

#### Files and Directories

Learn about the structure of the file system on Apple devices, and how to access that file system using the [`Foundation`](https://developer.apple.com/documentation/Foundation) framework. If you manage your app’s data using technologies such as [`SwiftData`](https://developer.apple.com/documentation/SwiftData), you might not work with files often. When you do, you need to know where to put them, and how to manage them efficiently. You also need to understand some of the special conventions that Apple platforms use to minimize the complexity of the file system for people using Apple devices.

#### Shared Data

Make your app’s data available where it’s needed — on one device or multiple devices. Place your data in iCloud to create a feeling of continuity for people moving from one device to the next. Similarly, share data between your app and one of your app extensions to keep your own content synchronized and up to date.

#### Personal Data

Apple devices can contain a lot of personal information, including contacts, photos, locations, health information, and more. People use the system apps to manage some of this data, but your app can also contribute to that data in a privacy friendly way. Let people know what data you plan to access.

## Topics

### Data structures
- [Standard data types and processes](standard-data-types-and-processes.md)
  Store fundamental types of data, and discover the key behaviors that make using those types easier.
- [Structured data models](structured-data-models.md)
  Build a structured data model for your app, and persist that data model to disk or iCloud.
### Persistence and sharing
- [Files and directories](files-and-directories.md)
  Navigate the file system on Apple devices, find important directories, and read and write your app’s documents and files.
- [Shared data](shared-data.md)
  Share data with your apps running on different devices using iCloud, or share data between your app and app extensions.
- [Personal data](personal-data.md)
  Access the personal data that people keep on their devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/data-management)*