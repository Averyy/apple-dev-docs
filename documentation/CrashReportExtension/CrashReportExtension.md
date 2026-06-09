# CrashReportExtension

**Framework**: CrashReportExtension  
**Kind**: module

Inspect crashed processes to create crash reports.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)

#### Overview

The Crash Report Extension framework allows you to perform analysis and produce a report when your app crashes. Your crash-handling code executes out-of-process, rather than from a signal handler or other in-process techniques.

You implement your handler by writing an app extension that conforms to the [`CrashReporterExtension`](crashreporterextension.md) protocol. The system calls your [`processCrashReport(process:)`](crashreporterextension/processcrashreport(process:).md) method when the app crashes. Use the [`CrashedProcess`](crashedprocess.md) parameter to inspect the state of the crashed app by retrieving a crash reason, symbolicating relevant addresses, and communicating with the process over a read-only Mach port. After collecting the crash data, you can send a report back to your own server.

As with all app extensions, your extension’s bundle identifier must be a child of the main app identifier. For example, for an app with bundle ID `com.example.myapp`, a crash reporter extension might use the identifiers `com.example.myapp.crash-handler` or `com.example.myapp.analytics.crashes`. In addition, your extension’s information property list needs to declare the extension point, as follows:

```xml
<dict>
    <key>EXAppExtensionAttributes</key>
    <dict>
        <key>EXExtensionPointIdentifier</key>
        <string>com.apple.crash-reporter.extension</string>
    </dict>
</dict>
```

Xcode adds an appropriate extension bundle identifier and information property list if you create your extension target with the Crash Report Extension template.

> **Note**: Crash Report Extension is available on iOS 27 and later. It isn’t available to Catalyst-based macOS apps, or on iOS apps running on Mac computers with Apple silicon.

## Topics

### Essentials
- [protocol CrashReporterExtension](crashreporterextension.md)
  The base type for crash reporter extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CrashReportExtension)*