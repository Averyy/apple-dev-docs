# Files and directories

**Framework**: Technology Overviews

Navigate the file system on Apple devices, find important directories, and read and write your app’s documents and files.

The file system stores data files, apps, and the operating system itself. All disks connected to a device — whether they’re connected physically to the device or connected over the network — contribute space to a single collection of files. To manage the large number of files, the file system organizes them hierarchically using directories. Although the directory hierarchy for most Apple platforms is similar, there are some minor differences from one platform to another.

Most disks attached to Apple devices use [`About Apple File System`](https://developer.apple.com/documentation/Foundation/about-apple-file-system) (APFS) for the underlying disk format. APFS offers modern features like cloning, snapshots, space sharing, fast directory sizing, atomic safe-save operations, and sparse files. Because disks can adopt file systems other than APFS, use system frameworks like [`Foundation`](https://developer.apple.com/documentation/Foundation) to access files and directories. These frameworks provide a consistent API that handles differences between disk formats.

#### File Directory and Bundle Concepts

Apple platforms adopt specific conventions for files and directories, and it’s easier to write file-related code when you know these conventions.

##### File Paths

To specify the location of a file or directory, create a [`URL`](https://developer.apple.com/documentation/Foundation/URL) with the path to the item. Build your path from the directory names that precede the item’s location. When creating paths, adopt the following best practices:

-  Some platforms require you to put files in [`Well-known directories`](files-and-directories#Well-known-directories.md), and starting your path with a well-known directory is always the best approach. For example, iOS apps put files into the app’s container directory. Choose one of these directories instead of building a path from the current working directory or the root of the file system.
-  When building a path from text strings, use a forward-slash (/) character to separate directory and filenames. You can use your string to create a corresponding [`URL`](https://developer.apple.com/documentation/Foundation/URL) for the file or directory.
-  APFS is case insensitive by default, but people can configure APFS to be case sensitive. Building your code to handle case-sensitive names lets you run safely on any system.
-  The system uses filename extensions to route files to appropriate apps. It also uses them as a hint for the file’s contents.
-  A file or directory can have a second name, known as its , which you show only from your app’s interface. The system shows [`displayName(atPath:)`](https://developer.apple.com/documentation/Foundation/FileManager/displayName(atPath:)) to create a more friendly view of the file system. For example, the display name for a file might hide the filename extension. If your app shows file and directory names in its interface, show display names when they’re available. Never use display names in file paths or in code that accesses the file system.

##### Well Known Directories

The system organizes system files, apps, and all other content into well-known locations, each with a specific purpose. Use each directory only for its intended purpose.

Get paths for other well-known directories from the [`URL`](https://developer.apple.com/documentation/Foundation/URL) or [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) type. macOS in particular has many more well-known directories, most of which people can access directly from the Finder or Terminal apps. You might use one of these locations in specific circumstances. For example, you might want to put an item directly into the home directory of the logged-in account. You rarely use these locations outside of macOS apps.

##### Bundles

A  is a directory that the system presents to people as a single file. Bundles simplify people’s interactions with apps, app extensions, and other bundled items. For example, interacting with an app launches that app instead of showing you the app’s code and resource files.

Bundle directories have specific structures, which are similar but can vary from one platform to another. In macOS, bundles are more hierarchical, with code, resources, and other types of content in dedicated directories. In iOS, iPadOS, tvOS, visionOS, and watchOS, bundles use a flatter organizational structure for simplicity. Bundle-related APIs use the platform-specific structure to locate resources. For example, when an app [`Supporting multiple languages in your app`](https://developer.apple.com/documentation/Xcode/supporting-multiple-languages-in-your-app), the APIs look for localized resources in language-specific project directories, which have an ISO 639 language code and an `.lproj` extension for the directory name.

Although bundles have a well-defined structure, you don’t need to know the details of this structure to create or use them. Xcode automatically creates bundle structures for you at build time, and places code and other resources in appropriate locations. To retrieve items from a bundle, use a [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) type to request the URL of the item you want first. This type searches the bundle for the requested resource, taking platform differences and language settings into account.

The Info pane of your project in Xcode also contains static information about your app’s [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List). Configure this file in Xcode by selecting it and using the associated editor to [`Managing Your App’s Information Property List`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

##### File Packages

Like a bundle, a  is a directory that the system presents to people as a single file. You use file packages to implement custom file formats, especially when those formats contain multiple different types of data. For example, a word processor document type that contains one or more files with text and separate files for images and media can keep those resources separate using a file package.

Unlike bundles, file packages have no predefined structure, so you’re responsible for determining the contents and organization of your app’s file packages. To define a custom document type, [`Managing Your App’s Information Property List`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list) to the Info pane of your project in Xcode. To turn a document type into a package, add the [`LSTypeIsPackage`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes/LSTypeIsPackage) key to its definition.

##### Asset Catalogs

An [`Managing assets with asset catalogs`](https://developer.apple.com/documentation/Xcode/managing-assets-with-asset-catalogs) is one of the best ways to manage resources in your app bundle. Asset catalogs help you organize the images icons, colors, and other resources your app uses. Depending on the device and system settings, your app might need to display images and colors with a several different appearances. For example, you might need to display light or dark versions of an image or one with a high contrast ratio. Asset catalogs let you gather all of these related resources under a single name in your app bundle. When you need a resource, you specify the name and the system provides the version of the resource that best matches the current settings.

![A screenshot of the UIKit catalog sample code project that shows one of the images in the project's asset catalog.](https://docs-assets.developer.apple.com/published/87cb298c66a5e5f21cdb3ce6f7010ad2/asset-catalog%402x.png)

#### Read Write and Manage Files and Directories

System-provided objects minimize the time you spend reading, writing, and managing files directly. In a document-based app, [`FileDocument`](https://developer.apple.com/documentation/SwiftUI/FileDocument), [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument), and [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) automatically read and write the underlying file for you, and support autosave operations and your app’s menus. Similarly, [`Image`](https://developer.apple.com/documentation/SwiftUI/Image), [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage), and [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) types read image files and provide you with an object you can use directly in your app. These types let you focus on using the data, and are often more efficient than managing the files yourself.

When working with custom file types, or files the system doesn’t natively support, you can still manage files and directories yourself. The [`Foundation`](https://developer.apple.com/documentation/Foundation) framework provides several types for reading and writing files, but the [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) provides your initial access to the file system. Use that object to find and create files and directories, read and write file attributes, and move items around the file system.

When you need to read and write files, you have several options. You can do so all at once using a [`Data`](https://developer.apple.com/documentation/Foundation/Data) type, or you can open a file and read it incrementally using a [`FileHandle`](https://developer.apple.com/documentation/Foundation/FileHandle) object or the POSIX APIs. If you have a custom type that uses a file package, manage the files in that package using a [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) object.

If your app shares files with other processes, [`Coordinate access to shared files`](shared-data#Coordinate-access-to-shared-files.md) to ensure file integrity. If your app shares files with an app extension or another process, or if you read and write files from someone’s iCloud storage, you must use file coordinators.

#### Download Large Files in the Background

When people buy your app from the App Store, they want to be able to download it quickly and try it out. If your app has large data files that it doesn’t need right away, consider downloading them separately after your app is already on someone’s device. A game might ship with the assets for the first level and download assets for other levels separately. Similarly, you might choose to download a large language model separately, so you can update it later.

To support background downloads, store your files on your company’s servers or on the App Store. Adopt the [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) framework and use it to schedule downloads. If your app needs files at first launch, configure a [`Configuring your Background Assets project`](https://developer.apple.com/documentation/BackgroundAssets/configuring-background-assets) for the system to download right away. Provide an [`Downloading essential assets in the background`](https://developer.apple.com/documentation/BackgroundAssets/downloading-essential-assets-in-the-background) to track the download progress of your app’s files.

#### Protect the Files You Create

Enable automatic encryption for files you create by assigning an appropriate [`URLFileProtection`](https://developer.apple.com/documentation/Foundation/URLFileProtection) to each one. The system stores your files encrypted on disk, making them accessible only under specific circumstances. For example, you might make files accessible only after someone unlocks their device. Choose a level of protection based on the type of data you’re saving, adopting more strict protection rules for sensitive or personal data.

> **Note**: If your app manages personal or sensitive information, consider [`Apple CryptoKit`](https://developer.apple.com/documentation/CryptoKit) for any data you store in files on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/files-and-directories)*