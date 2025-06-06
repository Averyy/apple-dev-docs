# Creating App Clip Codes with the App Clip Code Generator

**Framework**: Appclip

Use the App Clip Code Generator command-line tool to verify your code’s colors, get color suggestions, and create App Clip Codes.

#### Overview

By placing an App Clip Code at a physical location or using it in printed or digital marketing materials, you make your App Clip more discoverable. An App Clip Code always uses a design Apple provides, and users instantly recognize and scan it to launch your App Clip. Use the App Clip Code generator command-line tool to create App Clip Codes during development of your App Clip or to automate the creation of App Clip Codes.

> **Note**:  You must be enrolled in the Apple Developer Program before you can download the App Clip Code Generator. For information about the Apple Developer Program, see [`How the Program Works`](https://developer.apple.comhttps://developer.apple.com/programs/how-it-works/).

With the App Clip Code Generator command-line tool, you can:

- Get color suggestions for your App Clip Code.
- Experiment with custom colors.
- Verify a custom color pair.
- Save your generated App Clip Codes as Scalable Vector Graphics (SVG) files.

Use the generated SVG files to test your App Clip’s launch experience during development and to create App Clip Codes for use at physical locations, in digital communications, and so on. For design and printing guidance, see [`Human Interface Guidelines > App Clips > App Clip Codes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/app-clip-codes/).

If you already created an advanced App Clip experience in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/) and prefer a tool with a more visual interface, you can use App Store Connect to create the App Clip Code. For more information, see [`Creating App Clip Codes with App Store Connect`](creating-app-clip-codes-with-app-store-connect.md).

##### Install the App Clip Code Generator

To download and install the App Clip Code Generator, visit [`App Clips Resources`](https://developer.apple.comhttps://developer.apple.com/app-clips/resources/) and log into your Apple Developer account. After you download the App Clip Code Generator, open the downloaded disk image and run the package installer. You can find the installed tool at `/Library/Developer/AppClipCodeGenerator`.

##### Choose a Default Color Pair

App Clip Codes use three different colors: a foreground color and a background color you choose, and a third color that the command-line tool generates for you based on the other two colors. To ensure that users can reliably scan the App Clip Code, the color combination must offer enough contrast. Apple offers default color templates to help you choose a color pair.

![Illustration of an App Clip Code with callouts for background, foreground, and generated colors.](https://docs-assets.developer.apple.com/published/43bb6f81cb86f8b97a45af95fd284152/media-3706534%402x.png)

To see the list of default color pairs, open the Terminal app and run the `templates` command:

```shell
% AppClipCodeGenerator templates
```

This command prints an index and a hexadecimal representation of the foreground and background colors for each default color pair.

```other
Index: 0 Foreground: FFFFFF Background: 000000
Index: 1 Foreground: 000000 Background: FFFFFF
Index: 2 Foreground: FFFFFF Background: 777777
Index: 3 Foreground: 777777 Background: FFFFFF
Index: 4 Foreground: FFFFFF Background: FF3B30
Index: 5 Foreground: FF3B30 Background: FFFFFF
Index: 6 Foreground: FFFFFF Background: EE7733
Index: 7 Foreground: EE7733 Background: FFFFFF
Index: 8 Foreground: FFFFFF Background: 33AA22
Index: 9 Foreground: 33AA22 Background: FFFFFF
Index: 10 Foreground: FFFFFF Background: 00A6A1
Index: 11 Foreground: 00A6A1 Background: FFFFFF
Index: 12 Foreground: FFFFFF Background: 007AFF
Index: 13 Foreground: 007AFF Background: FFFFFF
Index: 14 Foreground: FFFFFF Background: 5856D6
Index: 15 Foreground: 5856D6 Background: FFFFFF
Index: 16 Foreground: FFFFFF Background: CC73E1
Index: 17 Foreground: CC73E1 Background: FFFFFF
```

To see a preview of App Clip Codes for each default color pair as a PNG file, use the Finder or Terminal app to navigate to `/Library/Developer/AppClipCodeGenerator/SampleTemplates`.

##### Experiment with Custom Colors

In addition to choosing a default color pair, you can choose custom foreground and background colors. To help you choose a color pair that offers high contrast, the App Clip Code Generator tool includes functionality to verify your custom color pair. It also suggests alternative colors in case the ones you initially choose don’t offer enough contrast.

To verify your custom color pair, run the `suggest` command in Terminal:

```shell
% AppClipCodeGenerator suggest --foreground $foregroundColor --background $backgroundColor
```

Replace the values for the `--foreground` and `--background` arguments with your RGB color’s hexadecimal representation; for example:

```shell
% AppClipCodeGenerator suggest --foreground 65D212 --background 5B1637
```

Doing so prints the color combination you entered as `Foreground: 65D212 Background: 5B1637` to confirm that the chosen color pair offers enough contrast to allow for reliable scanning of the App Clip Code.

If you provide a color pair that doesn’t offer enough contrast (for example, if you run `AppClipCodeGenerator suggest --foreground 123456 --background 345678`), the tool prints a list of suggested color pairs.

```other
Foreground: FFFFFF Background: 345678
Foreground: 44DDDD Background: 345678
Foreground: 55DDFF Background: 345678
Foreground: AABBCC Background: 345678
Foreground: BBCCBB Background: 345678
Foreground: FFBBEE Background: 345678
Foreground: 33DDFF Background: 345678
Foreground: CCBB33 Background: 345678
```

Note how the tool suggests foreground colors based on the chosen background color.

##### Generate Your App Clip Code

When you’ve decided on the invocation URL and the color pair, use the App Clip Code Generator tool to create an App Clip Code and save it as an SVG vector graphic file. Open the Terminal app, then create an App Clip Code with the tool’s `generate` command, using one of the following options:

- To generate a scan-only App Clip Code that uses the badge design and a default color pair, use the `--index` option with the index of the default color pair as its value; for example:

```shell
% AppClipCodeGenerator generate --url https://appclip.example.com --index 9 --output ~/path/to/filename.svg
```

- To generate an App Clip Code without the App Clip logo, use the `--logo` option and pass `none` to it; for example:

```shell
% AppClipCodeGenerator generate --url https://appclip.example.com --index 9 --logo none --output ~/path/to/filename.svg
```

- To generate an SVG file for an NFC-integrated App Clip Code, set the `--type` option to `nfc`; for example:

```shell
% AppClipCodeGenerator generate --url https://appclip.example.com --index 9 --output ~/path/to/filename.svg --type nfc
```

- To generate an App Clip Code with a custom color pair, set both the `--foreground` and `--background` options to use your custom colors; for example:

```shell
% AppClipCodeGenerator generate --url https://appclip.example.com --foreground 123456 --background FFFFFF --output ~/path/to/filename.svg
```

To see all available commands and options, run `AppClipCodeGenerator --help`.

App Clip Codes can only encode a limited amount of information. The App Clip Code Generator displays an error message if you choose an invocation URL that exceeds the amount of encodable information or if it contains invalid characters. For more information, see [`Encoding a URL in an App Clip Code`](encoding-a-url-in-an-app-clip-code.md). For general information about choosing an App Clip’s invocation URL, see [`Configuring the launch experience of your App Clip`](configuring-the-launch-experience-of-your-app-clip.md).

Use the SVG file to test your App Clip invocations locally, add it to your digital and print media, or create NFC-integrated App Clip Codes. Print your App Clip Codes yourself, or work with a professional printing service — for example, [`RR Donnelley`](https://developer.apple.comhttps://touchless.acc.rrd.com/). For printing guidance, see [`Preparing multiple App Clip Codes for production`](preparing-multiple-app-clip-codes-for-production.md) and [`Human Interface Guidelines > App Clips > Printing Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/printing-guidelines/).

##### Automate the Creation of App Clip Codes

If you need to create many different App Clip Codes, consider automating their creation. The App Clip Code Generator comes with a Python script and a comma-separated values (CSV) file to use with it. The CSV file contains sample data to use to create App Clip Codes. You can find the script and the CSV file at `/Library/Developer/AppClipCodeGenerator/Scripts`.

The following code shows a CSV file that contains the information for four App Clip Codes:

```other
SVG File Name,URL,Background Color,Foreground Color,Type,Logo
camera_standalone.svg,https://appclip.example.com,FFFFFF,000000,cam,none
nfc_standalone.svg,https://appclip.example.com,FFFFFF,000000,nfc,none
camera_badge.svg,https://appclip.example.com,FFFFFF,000000,cam,badge
nfc_badge.svg,https://appclip.example.com,FFFFFF,000000,nfc,badge
```

To create a batch of App Clip Codes:

1. Navigate to `/Library/Developer/AppClipCodeGenerator/Scripts` in the Finder or Terminal app, and copy its contents to a location of your choice; for example, a directory named `AppClipCodes` in your app’s Git repository.
2. Navigate to the directory that contains the copied files and review its contents. Then, create a new directory where you want to save the App Clip Codes you’ll create in the next step. For example, you might create a directory named `GeneratedCodes`.
3. In the Terminal app, navigate to the directory that contains the copied files.
4. From within the directory, run the Python script:

```shell
% python batch_generator.py $filename.csv $directory
```

Replace the placeholders with the actual file and directory names. If you used the file and directory names mentioned in the previous steps, run the following command:

```shell
% python batch_generator.py sample_list.csv GeneratedCodes
```

Doing so generates four App Clip Codes using the data in the CSV file and saves them in the `GeneratedCodes` directory. 5. Review the generated App Clip Codes, then modify the `sample_list.csv` file as necessary to generate your App Clip Codes. Note that for the script to work, you can’t change the names of the CSV file’s fields.

![Screenshot of a Finder window that shows the file structure of a directory named AppClipCodes. The folder contains files you copied from the Scripts folder. It also contains a new directory named GeneratedCodes that contains generated App Clip Codes.](https://docs-assets.developer.apple.com/published/c89a60427bde7627ab0382ce610a15fb/media-3706526%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppClip/creating-app-clip-codes-with-the-app-clip-code-generator)*