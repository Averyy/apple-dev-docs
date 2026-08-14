# TN3110: Resolving generic Xcode archive issue

**Framework**: Technotes

Identify common configurations that cause a generic Xcode archive.

#### Overview

The Archives organizer reports your archive as an *app archive* if it contains a single top-level app and a *generic Xcode archive*, otherwise. ![A generic archive.](/images/com.apple.technotes/tn3110-generic_archive@2x.png) You can validate and distribute an app archive. A generic archive, which may contain unexpected items such as header files, static libraries, or frameworks, can’t be validated nor distributed.

#### Ensure the Skip Install Build Setting Is Properly Configured

The [`Skip Install (SKIP_INSTALL)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/itcaec37c2a6) build setting determines whether to install built products within the archive.

When enabled for an app, Xcode doesn’t install the app within the archive. The produced archive doesn’t contain the single top-level app as expected. To generate an app archive, confirm that Skip Install is disabled for your app. ![Disable Skip Install for apps.](/images/com.apple.technotes/tn3110-skip_install_apps@2x.png)

When disabled for an app’s dependencies such as frameworks, Xcode adds these dependencies to the app’s archive. The produced archive contains multiple folders rather than the expected single top-level app. To generate an app archive, confirm that Skip Install is enabled for all your app’s dependencies. ![Enable Skip Install for dependencies.](/images/com.apple.technotes/tn3110-skip_install_dependencies@2x.png)

#### Use a Copy Files Build Phase

If your app links against static libraries, confirm that they all use a [`Copy files`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev50bab713d) build phase to export their header files. The produced app archive contains header files when static libraries use a [`Copy files`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev50bab713d) build phase to export these files.

#### Ensure the Installation Directory Build Setting Is Properly Configured

The [`Installation Directory (INSTALL_PATH)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/itcaec37c2a6?sub=devabd541cd5) build setting specifies the directory where to install built products. It takes default values according to the product being built. To generate an app archive, confirm that Installation Directory is set to the default value such as `$(LOCAL_APPS_DIR)` for apps.

#### Revision History

- **2022-02-08** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3110-resolving-generic-xcode-archive-issue)*